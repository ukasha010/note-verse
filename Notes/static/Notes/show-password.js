const checkBox = document.getElementById("show");
const passType = document.querySelector('input[type="password"]');
checkBox.addEventListener("change", function() {
  if (checkBox.checked) {
    passType.setAttribute("type", "text");
  } else {
    passType.setAttribute("type", "password");
  }
});