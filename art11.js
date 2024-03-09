let marks={
    amit:99,
    prashant:40,
    ajay:60,
    tushra:60,
}
for(let i=0;i<Object.keys(marks).length;i++){
    if(marks[Object.keys(marks)[i]]>50){
        console.log(Object.keys(marks)[i]+"="+marks[Object.keys(marks)[i]]); 

    }
   // console.log(Object.keys(marks)[i]+"="+marks[Object.keys(marks)[i]]);
}