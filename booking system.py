class BookingSystem:
    def __init__(self, booking_ID, property, guest, checkin_date, checkout_date):
        self.availability = None
        self.booking_status = "cancelled"
        self.id = booking_ID
        self.property = property
        self.guest = guest
        self.checkin = checkin_date
        self.checkout = checkout_date

    def book_property(self):
        if self.availability == 'available':
            print('booking property...')
            self.booking_status = "confirmed"
            self.availability = 'not available'
        else:
            self.booking_status = "cancelled"
