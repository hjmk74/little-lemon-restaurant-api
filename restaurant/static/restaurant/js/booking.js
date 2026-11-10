const bookingForm = document.querySelector("#booking-form");
const bookingMessage = document.querySelector("#booking-message");

if (bookingForm) {
    const dateInput = bookingForm.querySelector('[name="reservation_date"]');
    const slotInput = bookingForm.querySelector('[name="reservation_slot"]');
    const today = new Date();
    const localToday = new Date(today.getTime() - today.getTimezoneOffset() * 60000)
        .toISOString()
        .slice(0, 10);

    dateInput.min = localToday;

    bookingForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        bookingMessage.textContent = "Sending your request...";

        const formData = new FormData(bookingForm);
        const booking = Object.fromEntries(formData.entries());
        booking.reservation_slot = Number(booking.reservation_slot);

        try {
            const response = await fetch("/api/bookings/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(booking),
            });
            const result = await response.json();
            if (!response.ok) {
                const message = Object.values(result).flat().join(" ");
                throw new Error(message || "We could not save your booking.");
            }
            bookingMessage.textContent = "Your table request has been received. Thank you!";
            bookingForm.reset();
            dateInput.min = localToday;
        } catch (error) {
            bookingMessage.textContent = error.message;
        }
    });
}
