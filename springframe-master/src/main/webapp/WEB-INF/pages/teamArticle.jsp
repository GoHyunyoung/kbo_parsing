<%--
  Created by IntelliJ IDEA.
  User: moonlight
  Date: 2016. 9. 11.
  Time: 오후 9:23
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title></title>
    <link href="/resources/assets/css/index.css" rel="stylesheet" type="text/css">
    <!-- END THEME STYLES -->
    <%--BEGIN INDEX_PAGE SCRIPT--%>
    <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script type="text/javascript" src="/resources/assets/javascript/scroll.js"></script>
    <script type="text/javascript" src="/resources/assets/javascript/index.js"></script>
    <%--END INDEX_PAGE SCRIPT--%>
</head>
<body>
<%--
<c:set var="date" value="${article.date}"></c:set>
<c:forEach var="article" items="${articleArrayList}" varStatus="status">
    <li class=timeline id="${article.id}" hidden>
        <div class="timeline-time">
            <c:choose>
                <c:when test="${date==article.date}"></c:when>
                <c:otherwise>
            <span class="time" style='color: #303a41'>
                ${article.date.substring(4,6)}월
                ${article.date.substring(6,8)}일
                ${article.date.substring(8,article.date.length())}
            </span>
                </c:otherwise>
            </c:choose>
            <c:set var="date" value="${article.date}"></c:set>
        </div>
        <div class="timeline-icon"></div>
        <div class="timeline-body" data-name="${article.emblem}">
            <h2>${article.head}</h2>
            <div class="timeline-content">
                <img class="timeline-img pull-left"
                     src=${String.format("/resources/images/emblem_image/emblemB_%s.png",article.emblem)} alt="${article.emblem}">
                    ${article.intro}
                <br/>
                    ${article.main}
                <br/>
                    ${article.conc}
            </div>
            <div class="timeline-footer">
                <a href="${article.url}"> <i class="m-icon-swapright m-icon-white"></i> 해당 경기 상세히 보러가기  </a>
            </div>
        </div>
    </li>
</c:forEach>
--%>
<h1>Hi</h1>
<c:forEach var="article" items="${aritlceArrayList}">
    <h3>${article.id}</h3>
</c:forEach>

</body>
</html>
