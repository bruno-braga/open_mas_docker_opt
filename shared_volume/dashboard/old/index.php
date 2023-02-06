<!-- CSS only -->
<!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"> -->
<!-- JavaScript Bundle with Popper -->
<!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
-->



<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.min.css">

<script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>

<script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>


<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <?php
  $out = array();
  foreach (glob('../jacamo/src/src/agt/list/*.asl') as $filename) {
    $p = pathinfo($filename);
    $out[] = $p['filename'];
  }

  // Method: POST, PUT, GET etc
  // Data: array("param" => "value") ==> index.php?param=value

  function CallAPI($method, $url, $data = false)
  {
      $curl = curl_init();

      switch ($method)
      {
          case "POST":
              curl_setopt($curl, CURLOPT_POST, 1);

              if ($data)
                  curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
              break;
          case "PUT":
              curl_setopt($curl, CURLOPT_PUT, 1);
              break;
          default:
              if ($data)
                  $url = sprintf("%s?%s", $url, http_build_query($data));
      }

      // Optional Authentication:
      // curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
      // curl_setopt($curl, CURLOPT_USERPWD, "username:password");

      curl_setopt($curl, CURLOPT_URL, $url);
      curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

      $result = curl_exec($curl);

      curl_close($curl);

      return $result;
  }

  // foreach ($out as $aa) {
  //   echo $aa;
  //   echo "<br>";
  // }

  echo "<center><h1>List of agents</h1></center>";
  echo '
  <table id="example" class="display" style="width:100%">
  <thead>
  <tr>
  <th>ID</th>
  <th>Sugar</th>
  <th>Metabolism</th>
  <th>Vision</th>
  <th>File</th>
  <th>Traveling Path</th>
  </tr>
  </thead>
  <tbody>
  ';

//$file_name = "netlogo_output/output.txt";
  $file_name =str_replace(["[","]", "\""],"", $_ENV["output_agents"]);

  if(file_exists($file_name)){
    $handle = fopen($file_name, "r");
    if ($handle) {
     $c = 0;
    // echo "<h1>List of all dead agents</h1>";
  		// echo '
  		// <table id="example" class="display" style="width:100%">
  		//   <thead>
  		//     <tr>
  		//       <th>ID</th>
  		//     <th>Sugar</th>
  		//     <th>Metabolism</th>
  		//     <th>Vision</th>
  		//     </tr>
  		//   </thead>
  		//   <tbody>
  	 //  ';

     while (($lines = fgets($handle)) !== false) {
       echo "<tr>";
       $c++;
          // process the line read.
          // echo $line;
       $line = explode(" ", $lines);

          #print_r($line);

          #print(sizeof($line));

          #print_r($line[1]."\n");

       $line = str_replace(']', ' ', $line);

          #print_r($line);

          #echo "att1: ".$line[1]."att2: ".$line[2]."att3: ".$line[3]."att4: ".$line[4]."\n";

       echo '<td class="ids">'.$line[1].'</td>';
       echo '<td>'.$line[2].'</td>';
       echo '<td>'.$line[3].'</td>';
       echo '<td class="vision">'.$line[4].'</td>';
       if (in_array(($line[1]), $out)) { 
        echo '<td>'."<button value='".$line[1]."' class='btnSubmit buttonSubmit' type='button'>".$line[1]."</button>".'</td>';
       }
       else
        echo '<td><button>'."No File".'</button></td>';
       echo '<td>'.$line[5].'</td>';
       echo "</tr>";

          // foreach ($line as $word) {
          // 	echo "att1: ".$word[1]."att2: ".$word[2]."att3: ".$word[3]."att4: ".$word[4]."\n";
          // }
     }

     fclose($handle);
     $file_name = "/shared_volume/netlogo_output/general_send_agent.txt";

      if(file_exists($file_name)){
        $handle = fopen($file_name, "r");
        if ($handle) {
         $c = 0;
        // echo "<h1>List of all dead agents</h1>";
          // echo '
          // <table id="example" class="display" style="width:100%">
          //   <thead>
          //     <tr>
          //       <th>ID</th>
          //     <th>Sugar</th>
          //     <th>Metabolism</th>
          //     <th>Vision</th>
          //     </tr>
          //   </thead>
          //   <tbody>
         //  ';

         while (($lines = fgets($handle)) !== false) {
           echo "<tr>";
           $c++;
              // process the line read.
              // echo $line;
           $line = explode(" ", $lines);

              #print_r($line);

              #print(sizeof($line));

              #print_r($line[1]."\n");

           $line = str_replace(']', ' ', $line);

              #print_r($line);

              #echo "att1: ".$line[1]."att2: ".$line[2]."att3: ".$line[3]."att4: ".$line[4]."\n";

           echo '<td class="ids">'.$line[1].'</td>';
           echo '<td>'.$line[2].'</td>';
           echo '<td>'.$line[3].'</td>';
           echo '<td class="vision">'.$line[4].'</td>';
           if (in_array(($line[1]), $out)) { 
            echo '<td>'."<button value='".$line[1]."' class='btnSubmit buttonSubmit' type='button'>".$line[1]." - FILA</button>".'</td>';
           }
           else
            echo '<td><button>'."No File".'</button></td>';
           echo '<td>'.$line[5].'</td>';
           echo "</tr>";

              // foreach ($line as $word) {
              //  echo "att1: ".$word[1]."att2: ".$word[2]."att3: ".$word[3]."att4: ".$word[4]."\n";
              // }
         }

         fclose($handle);
       }
     }

     echo "
     </tbody>
     <tfoot>
     <tr>
     <th>ID</th>
     <th>Sugar</th>
     <th>Metabolism</th>
     <th>Vision</th>
     <th>File</th>
     <th>Traveling Path</th>
     </tr>
     </tfoot>
     </table>";

     echo "<center><h1>Biggest Path:</h1></center>";
     echo "<center><h3 id='biggest_path'></h3></center>";

      // echo "<br><br><br><br><center><h1>ID x Vision</h1></center>";

      // echo
      // "<div>
      //   <canvas id='myChart'></canvas>
      // </div>";

      #while(true){};
   }
 }
 ?>

 <br> <br>
 <center><h1>Conteúdo de Arquivo</h1></center>
  <pre id="contents" class="normal">Content of file will be load here when you press the button</pre>

  <!-- <script type="text/javascript">
    function populatePre(url) {
      var xhr = new XMLHttpRequest();
      xhr.onload = function () {
        document.getElementById('contents').textContent = this.responseText;
      };
      xhr.open('GET', url);
      xhr.send();
    }
    populatePre('../jacamo/src/src/agt/list/1.asl');
  </script> -->

 <style>
  tfoot input {
    width: 100%;
    padding: 3px;
    box-sizing: border-box;
  }

  pre {
    white-space: pre-wrap;       /* Since CSS 2.1 */
    white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
    white-space: -pre-wrap;      /* Opera 4-6 */
    white-space: -o-pre-wrap;    /* Opera 7 */
    word-wrap: break-word;       /* Internet Explorer 5.5+ */
  }
</style>


<script type="text/javascript">
  var ids = [];
  var vision = [];
  var final_array = [];

	// $(document).ready( function () {
	//     $('#example').DataTable();
	// } );

  $(document).ready(function() {
    //alert(files.includes('800'));
    // console.log(files);
    $(".buttonSubmit").click(function() {
      var fired_button = $(this).html();
      //alert("value: "+fired_button);

      var url = '../jacamo/src/src/agt/list/'+fired_button+'.asl';
      var xhr = new XMLHttpRequest();
      xhr.onload = function () {
        document.getElementById('contents').textContent = this.responseText;
      };
      xhr.open('GET', url);
      xhr.send();
    });

    $('#files_table').DataTable();
    // $(".btnSubmit").click(function(){
    //   var button = $(this).html();
    //   alert(button);

    //   var url = '../jacamo/src/src/agt/list/'+button+'.asl';
    //   var xhr = new XMLHttpRequest();
    //   xhr.onload = function () {
    //     document.getElementById('contents').textContent = this.responseText;
    //   };
    //   xhr.open('GET', url);
    //   xhr.send();
    // });


    // Setup - add a text input to each footer cell
    $('#example tfoot th').each( function () {
      var title = $(this).text();
      $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    } );

    // DataTable
    var table = $('#example').DataTable({
      initComplete: function () {
            // Apply the search
            this.api().columns().every( function () {
              var that = this;

              $( 'input', this.footer() ).on( 'keyup change clear', function () {
                if ( that.search() !== this.value ) {
                  that
                  .search( this.value )
                  .draw();
                }
              } );
            } );
          }
        });

  } );

  $('#example .ids').each(function() {
    // alert($(this).html());
    ids.push($(this).html())
  });

  $('#example .vision').each(function() {
    // alert($(this).html());
    vision.push($(this).html())
  });

  for(var i=0; i<vision.length; i++) {
    final_array.push({x: ids[i].replace(/\D/g, ""), y: vision[i].replace(/\D/g, "")});
  }

  // for(var i=0; i<final_array.length; i++) {
  //   console.log(final_array[i]);
  // }

  var maxlen=0;
  var tdLongest;
  $('table td').each(function(){
    if($(this).text().length > maxlen)
    {
      maxlen = $(this).text().length;
      tdLongest = $(this);
    }
  });

  // console.log(tdLongest.text());
  // console.log(maxlen);

  $('#biggest_path').text(tdLongest.text());

  //tdLongest.closest('tr').css('background-color','#A52A2A');

  const data = {
    datasets: [{
      label: 'ID x Vision',
      data: final_array,
    // data: [{
    //   x: -10,
    //   y: 0
    // }, {
    //   x: 0,
    //   y: 10
    // }, {
    //   x: 10,
    //   y: 5
    // }, {
    //   x: 0.5,
    //   y: 5.5
    // }],
    backgroundColor: 'rgb(255, 99, 132)'
  }],
};

const config = {
  type: 'scatter',
  data: data,
  options: {
    scales: {
      x: {
        type: 'linear',
        position: 'bottom',
        display: true,
        label: 'ID'
      },
      y: {
        display: true,
        label: 'Vision'
      }
    }
  }
};
</script>

