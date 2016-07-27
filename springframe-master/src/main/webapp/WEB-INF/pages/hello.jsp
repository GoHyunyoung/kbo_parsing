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
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/pages/css/timeline.css" rel="stylesheet" type="text/css"/>
    <!-- END PAGE LEVEL STYLES -->
    <!-- BEGIN THEME STYLES -->
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/css/components.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/css/plugins.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/css/layout.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/css/themes/default.css" rel="stylesheet" type="text/css" id="style_color">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/css/custom.css" rel="stylesheet" type="text/css">
    <!-- END THEME STYLES -->

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="/resources/assets/bootstrap-3.3.4/js/bootstrap.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
    <script type="text/javascript" src="/resources/assets/scollingjs/scrollingjs.js"></script>
</head>

<body>
<div class="portlet light">
    <div class="portlet-body">
        <div class="row">
            <div class="col-md-12">
                <ul class="timeline">
                    <%--<c:forEach var="i" begin="1" end="${articleMap.size()}" step="1">--%>
                    <c:forEach var="i" begin="1" end="9" step="1">
                        <li class=timeline>
                            <div class="timeline-time">
                                <c:choose>
                                    <c:when test="${articleMap.get(String.valueOf(i)).date != articleMap.get(String.valueOf(i-1)).date}">
                                        <span class="time" style='color: #303a41'>${articleMap.get(String.valueOf(i)).date}</span>
                                    </c:when>
                                </c:choose>
                            </div>
                            <div class="timeline-icon">
                            </div>
                            <div class="timeline-body" data-name="${articleMap.get(String.valueOf(i)).emblem}">
                                <h2>${articleMap.get(String.valueOf(i)).head}</h2>
                                <div class="timeline-content">
                                    <img class="timeline-img pull-left" src=${String.format("/resources/images/emblem_image/emblemB_%s.png",articleMap.get(String.valueOf(i)).emblem)} alt="${articleMap.get(String.valueOf(i)).emblem}">
                                        ${articleMap.get(String.valueOf(i)).intro}
                                    <br/><br/>
                                        ${articleMap.get(String.valueOf(i)).main}
                                </div>
                                <div class="timeline-footer">
                                    <a href="${articleMap.get(String.valueOf(i)).url}" class="nav-link pull-right">
                                        해당 경기 상세히 보러가기<i class="m-icon-swapright m-icon-white"></i>
                                    </a>
                                </div>
                            </div>
                        </li>
                    </c:forEach>
                    <li id="getMoreArticle" align="center">
                        <img src="/resources/images/page-loading.gif" id="loading-img" alt="Loading" width="180px"/>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
</body>

</html>