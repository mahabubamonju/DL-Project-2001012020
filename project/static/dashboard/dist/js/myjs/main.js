

var tbody = document.querySelector("tbody");
var pageUl = document.querySelector(".pagination");
var itemShow = document.querySelector("#itemperpage");
var tr = tbody.querySelectorAll("tr");
var emptyBox = [];
var index = 1;
// page show korbe
var itemPerPage = 5;

for(let i=0; i<tr.length; i++){
    emptyBox.push(tr[i]);
}
itemShow.onchange = giveTrPerPage;

function giveTrPerPage(){
    itemPerPage = Number(this.value);
    displayPage(itemPerPage);
    pageGenerator(itemPerPage);
    getElement(itemPerPage);
}

// ====================================================================
// Number show
// ====================================================================

function displayPage(limit){
    tbody.innerHTML = '';
    for(let i=0; i<limit; ++i){
        tbody.appendChild(emptyBox[i]);
    }
    const pageNum = pageUl.querySelectorAll('.list');
    pageNum.forEach(n=>n.remove());
}
displayPage(itemPerPage);

// ====================================================================
// ====================================================================

// ====================================================================
// next prev number show
// ====================================================================

function pageGenerator(getem) {
    const num_of_tr = emptyBox.length;
    if(num_of_tr <= getem){
        pageUl.style.display = 'none';
    }
    else
    {
        pageUl.style.display = 'flex';
        const num_of_page = Math.ceil(num_of_tr/getem);
        for(let i=1; i<=num_of_page; i++){
            const li = document.createElement('li');
            li.className = 'list';
            const a = document.createElement('a');
            a.href = '#';
            a.innerText = i;
            a.setAttribute('data-page',i);
            li.appendChild(a);
            pageUl.insertBefore(li, pageUl.querySelector('.next'));            
        }
    }
}
pageGenerator(itemPerPage);

// ====================================================================
// ====================================================================

// ====================================================================
// active number show
// ====================================================================

let pageLink = pageUl.querySelectorAll('a');
let lasrPage = pageLink.length - 2;

function pageRunner(page, items, lastPage, active) {
    for(button of page)
    {
        button.onclick = e=>
        {
            const page_num = e.target.getAttribute('data-page');
            const page_mover = e.target.getAttribute('id')
            if (page_num != null){
                index = page_num;
            }
            else
            {
                if (page_mover === 'next'){
                    index++;
                    if (index >= lastPage){
                        index = lastPage;
                    }
                }
                else
                {
                    index--;
                    if (index <= 1){
                        index = 1;
                    }
                }
            }
            pageMaker(index, items, active);
        }
    }
}

var pageLi = pageUl.querySelectorAll('.list')
pageLi[0].classList.add('active');
pageRunner(pageLink, itemPerPage, lastPage, pageLi);

// ====================================================================
// ====================================================================

// ====================================================================
// ( Number show / active )
// ====================================================================

function getElement(val){
    let pagelink = pageUl.querySelectorAll('a');
    let lastpage = pagelink.length - 2;
    let pageli = pageUl.querySelectorAll('.list');
    pageli[0].classList.add('active');
    pageRunner(pagelink, val, lastpage, pageli);
}

// ====================================================================
// ====================================================================

// ====================================================================
// prev and next button
// ====================================================================
function pageMaker(index, item_pre_page, activePage){
    const start = item_pre_page * index;
    const end = start + item_pre_page;
    const current_page = emptyBox.slice((start - item_pre_page), (end - item_pre_page));
    tbody.innerHTML = '';
    for (let i=0; i<current_page.length; i++){
        let item = current_page[i];
        tbody.appendChild(item);
    }
    Array.from(activePage).forEach((e)=>{
        e.classList.remove('active');
    });
    activePage[index - 1].classList.add('active');
}
// ====================================================================
// ====================================================================
