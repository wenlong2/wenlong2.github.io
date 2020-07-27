function doconvert() {
var ipt_year = document.getElementById("ipt_year").value;
var y = 1.0*ipt_year;
var ipt_month = document.getElementById("ipt_month").value;
var m = 1.0*ipt_month;
var ipt_day = document.getElementById("ipt_day").value;
var d = 1.0*ipt_day;
var ipt_hour = document.getElementById("ipt_hour").value;
var h = 1.0*ipt_hour;
var ipt_minute = document.getElementById("ipt_minute").value;
var n = 1.0*ipt_minute;
var ipt_second = document.getElementById("ipt_second").value;
var s = 1.0*ipt_second;

var julian_date =
367.0*y-Math.floor(7*(y+Math.floor((m+9)/12.))/4.)-Math.floor(3*Math.floor((y+(m-9.)/7.)/100.+1.)/4.)+Math.floor(275*m/9.)+d+1721028.5+h/24.+n/1440.+s/86400.;
if (y<1) {y=-1*(y-1);document.getElementById("res_jd").innerHTML = "JD for BC "+y+'/'+m+'/'+d+'-'+h+':'+n+':'+s+" is: "+julian_date;}
else {document.getElementById("res_jd").innerHTML = "JD for "+y+'/'+m+'/'+d+'-'+h+':'+n+':'+s+" is: "+julian_date;}

document.getElementById("res_jd2").innerHTML = "    "+julian_date;
}

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}
function isInt(n) {
   return n % 1 === 0;
}

function what_format(a,b,c){
  if (isNumeric(a)) {
    var dot_ind = a.indexOf('.');
      if (dot_ind < 0){var to_return = 'I'+(c-b);}
      else {var ndigit = a.length-dot_ind-1;var to_return = 'F'+(c-b)+'.'+ndigit;}
     }
  else {var to_return = 'A'+(c-b);}
  return to_return;
}

function what_format_c(a,b,c){
  if (isNumeric(a)) {
    var dot_ind = a.indexOf('.');
      if (dot_ind < 0){var to_return = '%'+(c-b)+'i';}
      else {var ndigit = a.length-dot_ind-1;var to_return = '%'+(c-b)+'.'+ndigit+'f';}
     }
  else {var to_return = '%'+(c-b)+'s';}
  return to_return;
}

function dofind() {
var space_pos = []
var element = []
var ipt_row = document.getElementById("ipt_row").value;
var ipts = ipt_row.split('');
var pos_s = 0;
var pos_e = 0;
var icount = 0;
while (pos_e < ipts.length && icount < 1000) {
icount = icount+1;
for (i = pos_e; i < ipts.length; i++) {
   var pos_s = i;
   if (ipts[i] != " ") {break;}
}
for (i = pos_s; i < ipts.length; i++) {
   var pos_e = i;
   if (ipts[i] == " ") {break;}
}
var foo='';
if (pos_e == (ipts.length-1)){
  for (j=pos_s; j<ipts.length; j++) {foo=foo+ipts[j];}
  element.push(foo);
  space_pos.push(pos_e+1);
  break;
  }
else{
    for (j=pos_s; j<pos_e; j++) {foo=foo+ipts[j];}
    element.push(foo);
    space_pos.push(pos_e);
    }
}

var idlfmt = "'(";
for (i=0;i<element.length;i++){
    if (i==0){ele_fmt = what_format(element[i],0,space_pos[i]);}
    else {ele_fmt = what_format(element[i],space_pos[i-1],space_pos[i]);}
    if (i<element.length-1) {idlfmt = idlfmt+ele_fmt+',';}
    else {idlfmt = idlfmt+ele_fmt;}
  }
idlfmt = idlfmt+")'";


var rfmt = "c('";
for (i=0;i<element.length;i++){
    if (i==0){ele_fmt = what_format(element[i],0,space_pos[i]);}
    else {ele_fmt = what_format(element[i],space_pos[i-1],space_pos[i]);}
    if (i<element.length-1) {rfmt = rfmt+ele_fmt+"','";}
    else {rfmt = rfmt+ele_fmt;}
  }
rfmt = rfmt+"')";
rfmt = "Not support now";
<!-- One may use read.fwf() instead and forget read.fortran() -->


cfmt = "'";
for (i=0;i<element.length;i++){
  if (i==0){ele_fmt = what_format_c(element[i],0,space_pos[i]);}
  else {ele_fmt = what_format_c(element[i],space_pos[i-1],space_pos[i]);}
  cfmt = cfmt + ele_fmt;
}
cfmt = cfmt + "'";


fwffmt = "width=c(";
for (i=0;i<element.length;i++){
  if (i==0){ele_fmt = space_pos[i];}
  else {ele_fmt = "," + (space_pos[i] - space_pos[i-1]);}
  fwffmt = fwffmt + ele_fmt;
}
fwffmt = fwffmt + ")";


document.getElementById("idl_fmt").innerHTML = 'fmt = '+idlfmt;
<!-- document.getElementById("r_fmt").innerHTML = rfmt; -->
document.getElementById("clike_fmt").innerHTML = 'fmt = '+cfmt;
document.getElementById("rfwf_fmt").innerHTML = fwffmt;
document.getElementById("element").innerHTML = "Elements:    " + element;
document.getElementById("space_pos").innerHTML = "End positions:    " + space_pos;
}

