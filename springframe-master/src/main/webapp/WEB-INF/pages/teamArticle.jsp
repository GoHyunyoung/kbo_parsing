<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%--
  Created by IntelliJ IDEA.
  User: moonlight
  Date: 2016. 9. 11.
  Time: 오후 9:23
  To change this template use File | Settings | File Templates.
--%>
<html>
<head>
</head>
<body>
<c:forEach var="article" items="${articleArrayList}" varStatus="status">
    <li class="timeline" hidden="">
        <div class="teamTime">
            <span class="time" style='color: #303a41'>
                    ${article.date.substring(4,6)}월
                    ${article.date.substring(6,8)}일
                    ${article.date.substring(8,article.date.length())}
            </span>
        </div>
        <div class="timeIcon"></div>
        <div class="timeBody" data-name="${teamName}">
            <h2>${article.head}</h2>
            <div class="timeContent">
                ${article.intro}<br/>
                ${article.main}<br/>
                ${article.conc}
            </div>
            <div><div></div>
                <div align="right">
                    <a href="${article.url}"> <i class="m-icon-swapright m-icon-white"></i><i>해당 경기 상세히 보러가기</i> </a>
                </div>
            </div>
        </div>
    </li>
</c:forEach>
</body>
</html>
