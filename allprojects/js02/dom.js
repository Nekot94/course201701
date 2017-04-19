// alert('Шмель выйдет');
console.log('311635');
document.getElementById('da').innerHTML = "Шмель не выйдет";
console.log(document.body);
console.log(document.body.firstElementChild.innerHTML);
console.log(document.body.lastElementChild.tagName);
console.log(document.body.lastElementChild.previousElementSibling.innerHTML);
console.log(document.getElementsByClassName('rrr')[0].innerHTML);
var divs = document.getElementsByTagName('div'); 
for (var i = 0; i < divs.length; i++){
	console.log(divs[i].innerHTML);
}
document.querySelector('div#da').style.color = 'wheat';
document.querySelector('.rrr').setAttribute("title","Вкусный борщ");
function da() {
	alert("da!!!!!!");


}
function net(object) {

	object.style.color = 'blue';
}