function checkFormSubmission() {
  if (sessionStorage.getItem('formSubmitted')) {
    sessionStorage.removeItem('formSubmitted');
  }
}
function validateForm(event) {
event.preventDefault();
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
var errorMessage = "";

if (username.trim() === "") {
  errorMessage += "Username can't be null\n";
}
if (password.trim()=== "") {
  errorMessage += "Password can't be null";
} else if (password.length < 6) {
  errorMessage += "Password must be at least 6 characters long. ";
}
if (errorMessage) {
  alert(errorMessage);
} else {
  sessionStorage.setItem('formSubmitted', 'true');
  event.target.submit();
}
}
document.getElementById('loginForm').addEventListener('submit', validateForm);
window.addEventListener('load', checkFormSubmission);
window.onpageshow = function(event) {
if (event.persisted) {
  sessionStorage.removeItem('formSubmitted');
}
};