$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='enroll']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      FName: "required",
      LName: "required",
      country: "required",
      phonenumber: {
        required: true,
        minlength: 10
      },
      // dob: "required",
      address1: "required",
      state: "required",
      pincode: {
        required: true,
        minlength: 5
      },
      College: "required",
      Stream: "required"
    },
    // Specify validation error messages
    messages: {
      FName: "Please enter your First Name",
      LName: "Please enter your Last Name",
      country: "Please Select a Country",
      phonenumber: {
        required: "Please provide your Phone Number",
        minlength: "Phone Number must be at least 10 characters long"
      },
      address1: "Please enter your Address",
      // dob: "Please choose your Date of Birth",
      state: "Please enter a valid state name",
      pincode: {
        required: "Please enter your area pincode",
        minlength: "pincode must be at least 6 characters long"
      },
      College: "Please Enter your College Name",
      Stream: "Please Enter the choosed Stream"
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      // form.submit(function(e) {
      //   e.preventDefault();
      // });
      
      return false;
      // window.location.href="index.html";
    }
  });
});