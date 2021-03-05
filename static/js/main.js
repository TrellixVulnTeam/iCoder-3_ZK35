console.log('hello world')

const copyBtns = [document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

copyBtns.forEach(btn=>btn.addEventListener('clicked', ()=>{
	console.log('click')
}))

