<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>KBO Article Generator | Timeline</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/resources/assets/bootstrap-3.3.4/css/bootstrap.min.css">

    <link href="http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700&subset=all" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/simple-line-icons/simple-line-icons.min.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/uniform/css/uniform.default.css" rel="stylesheet" type="text/css">
    <!-- END GLOBAL MANDATORY STYLES -->
    <!-- BEGIN PAGE LEVEL STYLES -->
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/pages/css/timeline.css" rel="stylesheet" type="text/css">
    <link rel="stylesheet" type="text/css" href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap-datepicker/css/datepicker3.css">
    <!-- END PAGE LEVEL STYLES -->
    <!-- BEGIN THEME STYLES -->
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/css/components.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/css/plugins.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/css/layout.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/css/themes/default.css" rel="stylesheet" type="text/css" id="style_color">
    <link href="/resources/assets/css/custom.css" rel="stylesheet" type="text/css">
    <!-- END THEME STYLES -->

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="/resources/assets/bootstrap-3.3.4/js/bootstrap.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
    <script type="text/javascript" src="/resources/assets/javascript/infinite_scroll.js"></script>
    <script type="text/javascript" src="/resources/assets/javascript/search.js"></script>
</head>

<body>
<!-- BEGIN HEADER -->
<div class="page-header">
    <!-- BEGIN HEADER TOP -->
    <div class="page-header-top">
        <div class="container">
            <!-- BEGIN LOGO -->
            <div class="page-logo">
                <a href="/"><img src="/resources/images/logo-default.png" alt="logo" class="logo-default"></a>
            </div>
            <!-- END LOGO -->
        </div>
    </div>
    <!-- END HEADER TOP -->

    <!-- BEGIN HEADER MENU -->
    <div class="page-header-menu">
        <div class="container">
            <!-- BEGIN HEADER SEARCH BOX -->
            <form class="search-form" action="search.jsp" method="GET">
                <div class="input-group input-medium date date-picker" data-date-format="dd-mm-yyyy" data-date-start-date="+0d">
                    <input type="text" class="form-control" readonly="">
                    <span class="input-group-btn">
                        <button class="btn default" type="button"><i class="fa fa-calendar"></i></button>
                    </span>
                </div>
            </form>

            <!-- END HEADER SEARCH BOX -->
            <!-- BEGIN MEGA MENU -->
            <div class="hor-menu ">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="/">Mr.Writer?</a>
                    </li>
                    <li>
                        <a href="/">Timeline</a>
                    </li>
                    <li>
                        <a href="/">BoxScore</a>
                    </li>
                    <li>
                        <a href="/">Etc</a>
                    </li>
                </ul>
            </div>
            <!-- END MEGA MENU -->
        </div>
    </div>
    <!-- END HEADER MENU -->
</div>
<!-- END HEADER -->
<!-- BEGIN PAGE CONTAINER -->
<div class="page-container">
    <!-- BEGIN PAGE HEAD -->
    <div class="page-head">
        <div class="container">
            <!-- BEGIN PAGE TITLE -->
            <div class="page-title">
                <h1>Timeline <small>Recent Article on the KBO  </small></h1>
            </div>
            <!-- END PAGE TITLE -->
        </div>
    </div>
    <!-- END PAGE HEAD -->
    <!-- BEGIN PAGE CONTENT -->
    <div class="page-content">
        <div class="container">
            <!-- BEGIN SAMPLE PORTLET CONFIGURATION MODAL FORM-->
            <div class="modal fade" id="portlet-config" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>
                            <h4 class="modal-title">Modal title</h4>
                        </div>
                        <div class="modal-body">
                            Widget settings form goes here
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn blue">Save changes</button>
                            <button type="button" class="btn default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                    <!-- /.modal-content -->
                </div>
                <!-- /.modal-dialog -->
            </div>
            <!-- /.modal -->
            <!-- END SAMPLE PORTLET CONFIGURATION MODAL FORM-->
            <!-- BEGIN PAGE BREADCRUMB -->
            <ul class="page-breadcrumb breadcrumb">
                <li>
                    <a href="#">Home</a><i class="fa fa-circle"></i>
                </li>
                <li class="active">
                    Timeline
                </li>
            </ul>
            <!-- END PAGE BREADCRUMB -->
            <!-- BEGIN PAGE CONTENT INNER -->

            <div class="portlet light">
                <div class="portlet-body">
                    <div class="row">
                        <div class="col-md-12">
                            <ul class="timeline">
                                <c:forEach var="article" items="${articleList}">
                                    <li class=timeline>
                                        <div class="timeline-time">
                                                <%--<c:out value="안녕하세요"></c:out>--%>
                                            <c:choose>
                                                <c:when test="${date==article.date}">
                                                    <c:set var="date" value="${article.date}"></c:set>
                                                </c:when>
                                                <c:otherwise>
                                                    <span class="time" style='color: #303a41'>${article.date.substring(4,6)}월${article.date.substring(6,8)}일${article.date.substring(8,article.date.length())}</span>
                                                </c:otherwise>
                                            </c:choose>
                                            <c:set var="date" value="${article.date}"></c:set>
                                        </div>
                                        <div class="timeline-icon">
                                        </div>
                                        <div class="timeline-body" data-name="${article.emblem}">
                                            <h2>${article.head}</h2>
                                            <div class="timeline-content">
                                                <img class="timeline-img pull-left" src=${String.format("/resources/images/emblem_image/emblemB_%s.png",article.emblem)} alt="${article.emblem}">
                                                    ${article.intro}
                                                <br/>
                                                    ${article.main}
                                            </div>
                                            <div class="timeline-footer">
                                                <a href="${article.url}" class="nav-link pull-right">
                                                    해당 경기 상세히 보러가기<i class="m-icon-swapright m-icon-white"></i>
                                                </a>
                                            </div>
                                        </div>
                                    </li>
                                </c:forEach>
                                <li id="getMoreArticle" align="center">
                                    <img src="/resources/images/page-loading.gif" id="loading-img" alt="Loading" width="180px" />
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <!-- END PAGE CONTENT INNER -->
        </div>
    </div>
    <!-- END PAGE CONTENT -->
</div>
<!-- END PAGE CONTAINER -->
<!-- BEGIN PRE-FOOTER -->
<div class="page-prefooter">
    <div class="container">
        <div class="row">
            <div class="col-md-3 col-sm-6 col-xs-12 footer-block">
                <h2>About</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam dolore.
                </p>
            </div>
            <div class="col-md-3 col-sm-6 col-xs12 footer-block">
                <h2>Subscribe Email</h2>
                <div class="subscribe-form">
                    <form action="#">
                        <div class="input-group">
                            <input type="text" placeholder="mail@email.com" class="form-control">
                            <span class="input-group-btn">
							<button class="btn" type="submit">Submit</button>
							</span>
                        </div>
                    </form>
                </div>
            </div>
            <div class="col-md-3 col-sm-6 col-xs-12 footer-block">
                <h2>Follow Us On</h2>
                <ul class="social-icons">
                    <li>
                        <a href="#" data-original-title="rss" class="rss"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="facebook" class="facebook"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="twitter" class="twitter"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="googleplus" class="googleplus"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="linkedin" class="linkedin"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="youtube" class="youtube"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="vimeo" class="vimeo"></a>
                    </li>
                </ul>
            </div>
            <div class="col-md-3 col-sm-6 col-xs-12 footer-block">
                <h2>Contacts</h2>
                <address class="margin-bottom-40">
                    Phone: 800 123 3456<br>
                    Email: <a href="mailto:info@metronic.com">info@metronic.com</a>
                </address>
            </div>
        </div>
    </div>
</div>
<!-- END PRE-FOOTER -->
<!-- BEGIN FOOTER -->
<div class="page-footer">
    <div class="container">
        2014 © Metronic. All Rights Reserved.
    </div>
</div>
<div class="scroll-to-top" style="display: none;">
    <i class="icon-arrow-up"></i>
</div>
<!-- END FOOTER -->
<!-- BEGIN JAVASCRIPTS(Load javascripts at bottom, this will reduce page load time) -->
<!-- BEGIN CORE PLUGINS -->
<!--[if lt IE 9]>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/respond.min.js"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/excanvas.min.js"></script>
<![endif]-->
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-1.11.0.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-migrate-1.2.1.min.js" type="text/javascript"></script>
<!-- IMPORTANT! Load jquery-ui-1.10.3.custom.min.js before bootstrap.min.js to fix bootstrap tooltip conflict with jquery ui tooltip -->
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-ui/jquery-ui-1.10.3.custom.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap-hover-dropdown/bootstrap-hover-dropdown.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-slimscroll/jquery.slimscroll.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery.blockui.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery.cokie.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/uniform/jquery.uniform.min.js" type="text/javascript"></script>
<!-- END CORE PLUGINS -->
<!-- BEGIN PAGE LEVEL PLUGINS -->
<script type="text/javascript" src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap-datepicker/js/bootstrap-datepicker.js"></script>
<script type="text/javascript" src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js"></script>
<!-- END PAGE LEVEL PLUGINS -->
<!-- BEGIN PAGE LEVEL SCRIPTS -->
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/scripts/metronic.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/scripts/layout.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/scripts/demo.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/admin/pages/scripts/components-pickers.js"></script>
<script src="/resources/assets/javascript/index.js"></script>
<!-- END PAGE LEVEL SCRIPTS -->

<script>
    jQuery(document).ready(function() {
        // initiate layout and plugins
        Metronic.init(); // init metronic core components
        Layout.init(); // init current layout
        Demo.init(); // init demo features
        ComponentsPickers.init();
    });
</script>
<!-- END JAVASCRIPTS -->
<!-- END BODY -->
</body>
</html>