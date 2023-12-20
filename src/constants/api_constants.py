# Add your constants here

# >>>>>>>>>>>>>normal constant
BASE_URL = "https://restful-booker.herokuapp.com"


# >>>>>>>>>>>normal functionmethod
def base_url():
    return "https://restful-booker.herokuapp.com"


# >>>>>>>>>>>>>>Class method
class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # update, put,patch,delete booking id
    # not static because  each testcase has different booking id

    @property
    def url_patch_put_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)
