import csv


f = open("index.html", "w")




strtemp ="""
<!DOCTYPE html>
<html>

<head>
	<title>EEC SIS Europe Links</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="bootstrap.css" rel="stylesheet">


<style>
div.cities {
    background-color: black;
    color: white;
    margin: 20px 0 20px 0;
    padding: 20px;
	text-align:center;
}
h1 {
    text-align: center;
}
.btn {
	margin-top: 30px !important;
    margin-right: 5px;
	margin-bottom: 30px !important;
}

</style>
</head>

    <body style='background-color:black;'>
    <div class='container'>
	<div class="row">
		<div class="col-sm-12">
			<div class="cities">
				<h2>Johnson Controls</h2>
				<h2>EEC/SIS Europe Links</h2>
			</div>
		</div>	
	</div>
	
	<div class="row">
		<div class="col-sm-12">
			<img class="img-responsive center-block" width="400" height="200" src="img/jci.png" />
		</div>
	</div>
	<div class="row">

	</div>
"""

f.write(strtemp)


i=0
with open('links.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    csvheading = next(read)
    for row in read :
       
        if i==0 :
            strtemp="""\n<div class="row">"""
            f.write(strtemp)
        
        strtemp="""
        	<div class="col-sm-3">
              <a href=""" + row[1] + """ target="_blank" class="btn btn-primary btn-lg center-block" role="button">"""+ row[0] + "</a>" +"""
            </div>\n"""

        f.write(strtemp)
       
        if i == 3 :
            strtemp="""</div>
            """
            f.write(strtemp)

        i=i+1
        if i > 3 :
            i=0



strtemp ="""
    </div>
</div>
</body>
</html>
\n"""

f.write(strtemp)
f.close()        