<!DOCTYPE html>
<!--[if IE 8]> <html lang="ko" class="ie8 no-js"> <![endif]-->
<!--[if IE 9]> <html lang="ko" class="ie9 no-js"> <![endif]-->
<!--[if !IE]><!-->
<html lang="ko">
<!--<![endif]-->
<!-- BEGIN HEAD -->
<head>
    <meta charset="utf-8"/>
    <title>KBO Article Generator | Timeline</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <meta content="" name="description"/>
    <meta content="" name="author"/>
    <!-- BEGIN GLOBAL MANDATORY STYLES -->
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700&subset=all" rel="stylesheet" type="text/css">
    <link href="./metronic_v3.3.0/theme/assets/global/plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="./metronic_v3.3.0/theme/assets/global/plugins/simple-line-icons/simple-line-icons.min.css" rel="stylesheet" type="text/css">
    <link href="./metronic_v3.3.0/theme/assets/global/plugins/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <link href="./metronic_v3.3.0/theme/assets/global/plugins/uniform/css/uniform.default.css" rel="stylesheet" type="text/css">
    <!-- END GLOBAL MANDATORY STYLES -->
    <!-- BEGIN PAGE LEVEL STYLES -->
    <link href="./metronic_v3.3.0/theme/assets/admin/pages/css/timeline.css" rel="stylesheet" type="text/css"/>
    <!-- END PAGE LEVEL STYLES -->
    <!-- BEGIN THEME STYLES -->
    <link href="./metronic_v3.3.0/theme/assets/global/css/components.css" rel="stylesheet" type="text/css">
    <link href="./metronic_v3.3.0/theme/assets/global/css/plugins.css" rel="stylesheet" type="text/css">
    <link href="./metronic_v3.3.0/theme/assets/admin/layout3/css/layout.css" rel="stylesheet" type="text/css">
    <link href="./metronic_v3.3.0/theme/assets/admin/layout3/css/themes/default.css" rel="stylesheet" type="text/css" id="style_color">
    <link href="./metronic_v3.3.0/theme/assets/admin/layout3/css/custom.css" rel="stylesheet" type="text/css">
    <!-- END THEME STYLES -->
    <link rel="shortcut icon" href="favicon.ico"/>
</head>
<!-- END HEAD -->
<!-- BEGIN BODY -->
<!-- DOC: Apply "page-header-menu-fixed" class to set the mega menu fixed  -->
<!-- DOC: Apply "page-header-top-fixed" class to set the top menu fixed  -->

<body>
<?php
$connect=mysqli_connect('link10th.cjwmbrma7nnv.ap-northeast-2.rds.amazonaws.com:3306','link10th','link1234');
mysqli_select_db($connect,"link10th");
?>
<div class="portlet light">
    <div class="portlet-body">
        <div class="row">
            <div class="col-md-12">
                <ul class="timeline">
                    <?php
                    $colorArr=array('yellow','red','blue','grey','green');
                    $sql="SELECT * FROM Article";
                    $result=mysqli_query($connect,$sql);
                    //                    while_loop begin
                    while($row=mysqli_fetch_array($result)){
                        if($row[date]==$tmp)
                            $row[date]=null;
                        else
                            $tmp=$row[date];
                        $timeline_color=$colorArr[mt_rand(0,4)];

//                        엠블럼img
                        if($row[winTeam]=='삼성')
                            $emblem='SS';
                        elseif ($row[winTeam]=='한화')
                            $emblem='HH';
                        elseif ($row[winTeam]=='SK')
                            $emblem='SK';
                        elseif ($row[winTeam]=='KIA')
                            $emblem='HT';
                        elseif ($row[winTeam]=='LG')
                            $emblem='LG';
                        elseif ($row[winTeam]=='두산')
                            $emblem='OB';
                        elseif ($row[winTeam]=='롯데')
                            $emblem='LT';
                        elseif ($row[winTeam]=='넥센')
                            $emblem='WO';
                        elseif ($row[winTeam]=='kt')
                            $emblem='KT';
                        else
                            $emblem='NC';
                        $img_dir="./img/emblemB_".$emblem.".png";
                        echo ("
                            <li class=timeline-$timeline_color>
                                <div class=\"timeline-time\">
                                    <span class=\"time\" style='color: #303a41'>$row[date]</span>
                               </div>
                               <div class=\"timeline-icon\">                            
                               </div>
                               <div class=\"timeline-body\">
                                    <h2>$row[head]</h2>
                                    <div class=\"timeline-content\">
                                        <img class=\"timeline-img pull-left\" src=\"./$img_dir\" alt=\"\">
                                         $row[pre]
                                    </div>
                                    <div class=\"timeline-footer\">
                                        <a href=\"$row[url]\" class=\"nav-link pull-right\">
                                            해당 경기 상세히 보러가기<i class=\"m-icon-swapright m-icon-white\"></i>
                                        </a>
                                    </div>
                                </div>
                            </li>
                            ");
                    }
                    //                    while_loop end
                    ?>
                </ul>
            </div>
        </div>
    </div>
</div>




</body>
</html>