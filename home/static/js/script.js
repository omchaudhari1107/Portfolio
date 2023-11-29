var options = {
  strings: ["Full-Stack Dev", "Programmer 👨‍💻", "Django Dev❤️", "Learner 🔍"],
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

const loaderContainer = document.getElementById('loader-wrapper');
console.log(loaderContainer)
window.addEventListener('load', () => {
  loaderContainer.style.display = 'none';
});