var options = {
  strings: ["Full-Stack Dev", "Intern", "Programmer👨‍💻", "Learner", "Django Dev❤️"],
  typeSpeed: 100,
  backSpeed: 100,
  backDelay: 1000,
  loop: true
};

var typed = new Typed('.multiple-filed', options);

function download() {
  var filePath = "static/pdf/Om%20Chaudhari%20CV.pdf";
  var fileName = "Om Chaudhari CV.pdf"; 
  var a = document.createElement('a');
  a.href = filePath;
  a.download = fileName;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}
