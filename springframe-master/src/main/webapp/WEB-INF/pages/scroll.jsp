<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%--
  Created by IntelliJ IDEA.
  User: gohyunyoung98
  Date: 16. 7. 25
  Time: 오후 5:19
  To change this template use File | Settings | File Templates.
  --%>
  <html>
  <head>
  </head>
  <body>
    <c:forEach var="article" items="${articleArrayList}">
    <c:set var="startIdx" value="0"/>
    <c:set var="endIdx" value="${urlCountArr[0]-1}"/>
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
        <c:forEach var="count" begin="1" end="${urlCountArr[status.index]}">
        <c:forEach var="urlArrayList" begin="${startIdx}" end="${endIdx}" items="${criticalVOD_urlArrayList}">
        <c:out value="startIdx : ${startIdx}"/><br/>
        <c:out value="endIdx : ${endIdx}"/><br/>
        <c:out value="count : ${count}"/><br/>
        <c:set var="startIdx" value="${endIdx+1}"/>
        <c:set var="count" value="${urlCountArr[status.index]}"/>
        <c:set var="endIdx" value="${startIdx+count-1}"/>
        <iframe width="400px" height="250px" src="${urlArrayList.vodUrl}"></iframe>
    </c:forEach>
</c:forEach>
<i class="m-icon-swapright m-icon-white"></i>
<a href="${article.url}"> 해당 경기 상세히 보러가기  </a>

</div>
</div>
</li>
</c:forEach>

</body>
</html>