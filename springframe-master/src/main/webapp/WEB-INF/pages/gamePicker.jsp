<%--
  Created by IntelliJ IDEA.
  User: moonlight
  Date: 2016. 8. 29.
  Time: 오후 5:09
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<html>
<head>
    <link href="/resources/assets/css/index.css" rel="stylesheet" type="text/css">
</head>
<body>
<c:forEach var="article" items="${articleArrayList}">
    <c:choose>
        <c:when test="${(date!=article.date) && (date!=null)}">
            <c:set var="date" value="NULL"></c:set>
        </c:when>
        <c:otherwise>
            <!-- GamePickerBox -->
            <a href="#">
                <li class="gamePickerBox" data-name="${article.emblem}" onclick="gamePicker(${article.id})">
                    <img class="left-img" src="/resources/images/emblem_image/emblemB_${article.awayT}.png" alt="${article.awayT}">
                    <span>${article.head.substring(3,5)}</span> <span>: </span>
                    <span>${article.head.substring(article.head.length() -2)}</span>
                    <img class="right-img" src="/resources/images/emblem_image/emblemB_${article.homeT}.png" alt="${article.homeT}">
                </li>
            </a>
            <c:set var="date" value="${article.date}"></c:set>
        </c:otherwise>
    </c:choose>
</c:forEach>

</body>
</html>

