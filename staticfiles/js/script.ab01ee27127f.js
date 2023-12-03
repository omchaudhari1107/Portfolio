var options = {
  strings: ["Full-Stack Dev", "Programmer 👨‍💻", "Django Dev❤️", "Learner 🔍"],
  typeSpeed: 100,
  backSpeed: 100,
  backDelay: 1000,
  loop: true
};

var typed = new Typed('.multiple-filed', options);

// function download() {
//   var filePath = "home/static/pdf/Om Chaudhari CV.pdf";
//   var fileName = "Om Chaudhari CV.pdf";
//   var a = document.createElement('a');
//   a.href = filePath;
//   a.download = fileName;
//   document.body.appendChild(a);
//   a.click();
//   document.body.removeChild(a);
// }
function download() {
  var filePath = "static/pdf/Om_Chaudhari_CV.pdf"; // Update with the correct relative path
  var fileName = "Om_Chaudhari_CV.pdf"; // Update with the correct file name and extension

  var a = document.createElement('a');
  a.href = filePath;
  a.download = fileName;

  // Appending to the body and clicking might not work in all scenarios
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

