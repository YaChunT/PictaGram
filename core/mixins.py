# from django.shortcuts import redirect
# from two_factor.views.mixins import OTPRequiredMixin as BaseOTPRequiredMixin

# class OTPRequiredMixin(BaseOTPRequiredMixin):
#     def dispatch(self, request, *args, **kwargs):
#         # Implement your custom logic here
#         # For example, check if user has completed OTP setup
#         if not request.user.is_verified():
#             # Redirect to OTP setup page
#             return redirect('signin')

#         # Continue to original view dispatch if OTP is verified
#         return super().dispatch(request, *args, **kwargs)


