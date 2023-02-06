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


<!-- <script type="text/javascript" src="jquery-3.5.1.js"></script>

<script type="text/javascript" src="2jquery.dataTables.min.js"></script> -->
<!-- #<link rel="stylesheet" type="text/css" href="jquery.dataTables.min.css"> -->


<?php
echo "<center><h1>List of agents</h1></center>";
    echo '
    <table id="myTable" class="display" style="width:100%">
      <thead>
        <tr>
          <th>ID</th>
          <th>Sugar</th>
          <th>Metabolism</th>
          <th>Vision</th>
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
  		// <table id="myTable" class="display" style="width:100%">
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
          echo '<td>'.$line[5].'</td>';
          echo "</tr>";

          // foreach ($line as $word) {
          // 	echo "att1: ".$word[1]."att2: ".$word[2]."att3: ".$word[3]."att4: ".$word[4]."\n";
          // }
      }

      fclose($handle);

      echo "</tbody></table>";

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


<!-- <table id="example">
  <thead>
    <tr>
      <th>Month</th>
      <th>Savings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>January</td>
      <td>$100</td>
    </tr>
    <tr>
      <td>February</td>
      <td>$80</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Sum</td>
      <td>$180</td>
    </tr>
  </tfoot>
</table> -->


<script type="text/javascript">
  var ids = [];
  var vision = [];
  var final_array = [];

	$(document).ready( function () {
	    $('#myTable').DataTable();
	} );

  $('#mytable .ids').each(function() {
    // alert($(this).html());
    ids.push($(this).html())
  });

  $('#mytable .vision').each(function() {
    // alert($(this).html());
    vision.push($(this).html())
  });

  for(var i=0; i<vision.length; i++) {
    final_array.push({x: ids[i].replace(/\D/g, ""), y: vision[i].replace(/\D/g, "")});
  }

  for(var i=0; i<final_array.length; i++) {
    console.log(final_array[i]);
  }

  var maxlen=0;
  var tdLongest;
  $('table td').each(function(){
      if($(this).text().length > maxlen)
      {
        maxlen = $(this).text().length;
        tdLongest = $(this);
      }
  });

  console.log(tdLongest.text());
  console.log(maxlen);

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

// var myChart = new Chart(
//     document.getElementById('myChart'),
//     config
//   );

//   setTimeout(function(){
//    window.location.reload(1);
// }, 5000);



// const labels = [
//   'January',
//   'February',
//   'March',
//   'April',
//   'May',
//   'June',
// ];
// const data = {
//   // labels: labels,
//   datasets: [{
//     label: 'Vision',
//     backgroundColor: 'rgb(255, 99, 132)',
//     borderColor: 'rgb(255, 99, 132)',
//     data: final_array,
//   }]
// };

//   const config = {
//   type: 'line',
//   data,
//   options: {}
// };

// var myChart = new Chart(
//     document.getElementById('myChart'),
//     config
//   );

// if($('#mytable .ids').length < 10000)
//     setTimeout(function(){
//      window.location.reload(1);
//   }, 5000);
</script>

