<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: gohyunyoung98
  Date: 16. 7. 25
  Time: 오후 5:19
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<c:forEach var="article" items="${articleList}">
    <li class=timeline>
        <div class="timeline-time">
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