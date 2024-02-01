# Function:	DayNumber
#
# Purpose:	Given a date in YYYY-MM-DD format, return the day number within that year (e.g., 2017-02-01 would return "32").
# Usage:		@Python( "DayNumber", <DateFieldName or date in YYYY-MM-DD format>)
# Example Equation:	The following example can be applied to the Sample-Detailed Sales database:
#			@Python( "DayNumber", @Dtoc(INV_DATE, "YYYY-MM-DD"))
# Return Value:	A string containing the day number of a specifed date within the specified year.
#
# DISCLAIMER:	This script is not supported under any CaseWare IDEA Inc. standard support program or service.
#		The sample script is provided AS IS without warranty of any kind. CaseWare IDEA disclaims all
#		implied warranties including, without limitation, any implied warranties of merchantability or of
#		fitness for a particular purpose. The entire risk arising out of the use or performance of the
#		sample script and documentation remains with you. In no event shall CaseWare IDEA, its authors, or
#		anyone else involved in the creation, production, or delivery of the script be liable for any
#		damages whatsoever (including, without limitation, damages for loss of business profits, business
#		interruption, loss of business information, or other pecuniary loss) arising out of the use of or
#		inability to use the sample script or documentation, even if CaseWare IDEA has been advised of the
#		possibility of such damages.

def DayNumber(arg1):
    import datetime
    try:
        d = datetime.datetime.strptime(str(arg1), '%Y-%m-%d').timetuple().tm_yday
    except:
        d = "!FORMAT should be YYYY-MM-DD"
    return str(d)
