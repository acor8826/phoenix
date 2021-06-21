from decimal import Decimal
from django.conf import settings
from Product.models import Product
#from coupons.models import Coupon

class Script(object):
	def __init__(self, request):
		if user is authenticated:
			self.session = request.session
        	script = self.session.get(settings.SCRIPT_SESSION_ID)
        	if not script:
            # save an empty cart in the session
            	script = self.session[settings.SCRIPT_SESSION_ID] = {}
        self.script = script
        # store current applied coupon
        self.coupon_id = self.session.get('coupon_id')