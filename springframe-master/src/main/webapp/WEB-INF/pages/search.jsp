<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">
<head>

</head>
<body>
<div class="page-container">
    <!-- BEGIN PAGE HEAD -->
    <div class="page-head">
        <div class="container">
            <!-- BEGIN PAGE TITLE -->
            <div class="page-title">
                <h1>Timeline
                    <small>Recent Article on the KBO</small>
                </h1>
            </div>
            <!-- END PAGE TITLE -->
        </div>
    </div>
    <!-- END PAGE HEAD -->
    <!-- BEGIN PAGE CONTENT -->
    <div class="page-content">
        <div class="container">
            <!-- BEGIN SAMPLE PORTLET CONFIGURATION MODAL FORM-->
            <div class="modal fade" id="portlet-config" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
                 aria-hidden="true">
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
                                <c:forEach var="searchResult" items="${searchResult}">
                                    <li class=timeline>
                                        <div class="timeline-time">
                                            <c:choose>
                                                <c:when test="${date==searchResult.date}">
                                                    <c:set var="date" value="${searchResult.date}"></c:set>
                                                </c:when>
                                                <c:otherwise>
                                                    <span class="time"
                                                          style='color: #303a41'>${searchResult.date.substring(4,6)}월${searchResult.date.substring(6,8)}일${searchResult.date.substring(8,searchResult.date.length())}</span>
                                                </c:otherwise>
                                            </c:choose>
                                            <c:set var="date" value="${searchResult.date}"></c:set>
                                        </div>
                                        <div class="timeline-icon">
                                        </div>
                                        <div class="timeline-body" data-name="${searchResult.emblem}">
                                            <h2>${searchResult.head}</h2>
                                            <div class="timeline-content">
                                                <img class="timeline-img pull-left"
                                                     src=${String.format("/resources/images/emblem_image/emblemB_%s.png",searchResult.emblem)} alt="${searchResult.emblem}">
                                                    ${searchResult.intro}
                                                <br/>
                                                    ${searchResult.main}
                                            </div>
                                            <div class="timeline-footer">
                                                <a href="${searchResult.url}" class="nav-link pull-right">
                                                    해당 경기 상세히 보러가기<i class="m-icon-swapright m-icon-white"></i>
                                                </a>
                                            </div>
                                        </div>
                                    </li>
                                </c:forEach>
                                <li id="getMoreArticle" align="center">
                                    <img src="/resources/images/page-loading.gif" id="loading-img" alt="Loading"
                                         width="180px"/>
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
</body>
</html>