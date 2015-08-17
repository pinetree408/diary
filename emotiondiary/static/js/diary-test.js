var day_of_week = new Array('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
var month_of_year = new Array('January','February','March','April','May','June','July','August','September','October','November','December');

//  DECLARE AND INITIALIZE VARIABLES
var Calendar = new Date();

var year = Calendar.getFullYear();     // Returns year
var month = Calendar.getMonth();    // Returns month (0-11)
var today = Calendar.getDate();    // Returns day (1-31)
var weekday = Calendar.getDay();    // Returns day (1-31)

var DAYS_OF_WEEK = 7;    // "constant" for number of days in a week
var DAYS_OF_MONTH = 31;    // "constant" for number of days in a month
var cal;    // Used for printing

Calendar.setDate(1);    // Start the calendar day at '1'
Calendar.setMonth(month);    // Start the calendar month at now

//Make Calendar
var calendar_start = '<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 BORDERCOLOR=BBBBBB>';
var TR_start = '<TR>';
var TR_end = '</TR>';
var TD_start = '<TD WIDTH="50" HEIGHT="100%"><CENTER>';
var TD_end = '</CENTER></TD>';

//cal = calendar_start + TR_start + '<TD>';
cal = '<TR><TD>';
cal += '<TABLE BORDER=1 CELLSPACING=0 CELLPADDING=2>';

var calendar_header_month = '' +
'<TR>' +
  '<TD COLSPAN="' + DAYS_OF_WEEK + '">' + 
    '<CENTER><B>' +
      month_of_year[month] + ' ' + year +
    '</CENTER></B>' + 
  '</TD>' + 
'</TR>';

var week_head = '';

for(index=0; index < DAYS_OF_WEEK; index++)
{
  week_head += TD_start + day_of_week[index] + TD_end;
}

var calendar_header_week = '' +
'<TR>' +
  week_head + 
'</TR>';

cal += calendar_header_month;
cal += calendar_header_week;

cal += TR_start;

// FILL IN BLANK GAPS UNTIL TODAY'S DAY
for(index=0; index < Calendar.getDay(); index++){
  cal += TD_start + '  ' + TD_end;
}

// LOOPS FOR EACH DAY IN CALENDAR
for(index=0; index < DAYS_OF_MONTH; index++)
{
  if( Calendar.getDate() > index )
  {
    // RETURNS THE NEXT DAY TO PRINT
    week_day = Calendar.getDay();

    // START NEW ROW FOR FIRST DAY OF WEEK
    if(week_day == 0){
      cal += TR_start;
    }
    
    if(week_day != DAYS_OF_WEEK)
    {

      // SET VARIABLE INSIDE LOOP FOR INCREMENTING PURPOSES
      var day  = Calendar.getDate();
      // PRINTS DAY
      cal += TD_start + '<TABLE>' + TR_start + TD_start + day + TD_end + TR_end + TR_start + TD_start + 'test' + TD_end + TR_end + '</TABLE>' +TD_end;
    }

    // END ROW FOR LAST DAY OF WEEK
    if(week_day == DAYS_OF_WEEK){
      cal += TR_end;
    }

  }
    // INCREMENTS UNTIL END OF THE MONTH
  Calendar.setDate(Calendar.getDate()+1);

}// end for loop

cal += '</TD></TR></TABLE></TABLE>';

//  PRINT CALENDAR
document.getElementById("calendar").innerHTML = cal;
