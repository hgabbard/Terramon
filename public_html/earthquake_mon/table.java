<script language="javascript" type="text/javascript">
<!--
var Root;
var xmlDoc=new ActiveXObject("microsoft.xmldom");
xmlDoc.load("/home/hunter.gabbard/Seismon_folders/all/H1EQMon/1109093646-1109151386/earthquakes/iris1109114458/earthquakes.xml");
function StartUp()
{    
    if(xmlDoc1.readyState=="4")
    {
        StartLoading();
    }
    else
        {
         alert("Loading operation could not start");
        }
}

function StartLoading()
{
    Root=xmlDoc.documentElement;
    your_element.innerText=Root.childNodes(0).text;
    your_element.innerText=Root.childNodes(1).text;
}

//-->
</script>
