function learnMore(){
    window.open('https://www.britannica.com/biography/Alexander-the-Great', '_blank')
}

function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth' 
    });
  }

  $(document).ready(function(){
    $("#secret").click(function(){
      $("#secretText").append("<h1>This is the secret!</h1>");
      $("#secretText").append("<img src='https://assets.puzzlefactory.com/puzzle/254/647/original.jpg' alt='Placeholder Image'>");
    });
  });

  function changeCSS() {
    var mainCssLink = document.getElementById('main-css');
    if (mainCssLink.href.includes('index.css')) {
      mainCssLink.href = "{{url_for('static', filename='alternate.css')}}";
    } else {
      mainCssLink.href = "{{url_for('static', filename='index.css')}}";
    }
  }
  

