name_list=document.getElementsByClassName('BillService__title__1_WYP BillService__wid-r1-c1__2wAM3')
amt_list=document.getElementsByClassName('BillService__title__1_WYP BillService__wid-r1-c2__5LweC')
cellno_list=document.getElementsByClassName('BillService__sub-title1__3pC9V BillService__wid-r2-c1__7-DjN')

// assert(infolist[0].childNodes[0].textContent=="Account summary")
// assert(amt_list.length==name_list.length)
// assert(cellno_list.length==name_list.length)

var arr=[]
for(let i=1;i<amt_list.length;i++){
	name=name_list[i].childNodes[0].textContent;
    amt=amt_list[i].childNodes[0].textContent.substring(1);
    cellno=cellno_list[i].childNodes[0].textContent;
    allinfo=[cellno,name,amt];
    arr.push(allinfo);
}
// console.log(cellno)
arr=arr.sort((a,b)=>a[0]<b[0]);
for(let i=0;i<arr.length;i++){
    arr[i]=arr[i].join(",");
}
out=arr.join("\n")
out
// console.log(arr)