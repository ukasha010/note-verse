document.addEventListener("DOMContentLoaded", function () {
    const checkBox = document.getElementById("show");
    const passwordInput1 = document.getElementById("id_password1");
    const passwordInput2 = document.getElementById("id_password2");
  
    checkBox.addEventListener("change", function () {
      const inputType = checkBox.checked ? "text" : "password";
      passwordInput1.type = inputType;
      passwordInput2.type = inputType;
    });
  });