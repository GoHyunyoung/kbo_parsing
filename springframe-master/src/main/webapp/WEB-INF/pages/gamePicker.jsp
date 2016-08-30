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
    <a href="#">
        <li class="gamePickerBox" data-name="${article.emblem}">
            <img class="left-img" src=${String.format("/resources/images/emblem_image/emblemB_%s.png",article.emblem)} alt="${article.emblem}">

            <span>${article.head.substring(3,4)} </span>
            <span>: </span>
            <span>${article.head.substring(11)}</span>

            <img class="right-img" src=${String.format("/resources/images/emblem_image/emblemB_%s.png",article.emblem)} alt="${article.emblem}">
        </li>
    </a>
</c:forEach>

</body>
</html>

