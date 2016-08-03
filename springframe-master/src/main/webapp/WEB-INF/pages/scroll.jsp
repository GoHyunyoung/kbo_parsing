<%@ page import="java.util.ArrayList" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: gohyunyoung98
  Date: 16. 7. 25
  Time: 오후 5:19
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<c:forEach var="i" begin="1" end="${articleList.length}" step="1">
    <li class=timeline>
        <div class="timeline-time">
            <c:choose>
                <c:when test="${articleList.get(i).date != articleList.get(i-1).date}">
                    <span class="time" style='color: #303a41'>${articleList.get(i).date}</span>
                </c:when>
            </c:choose>
        </div>
        <div class="timeline-icon">
        </div>
        <div class="timeline-body" data-name="${articleList.get(i).emblem}">
            <h2>${articleList.get(i).head}</h2>
            <div class="timeline-content">
                <img class="timeline-img pull-left" src=${String.format("/resources/images/emblem_image/emblemB_%s.png",articleList.get(i).emblem)} alt="${articleList.get(i).emblem}">
                    ${articleList.get(i).intro}
                <br/>
                    ${articleList.get(i).main}
            </div>
            <div class="timeline-footer">
                <a href="${articleList.get(i).url}" class="nav-link pull-right">
                    해당 경기 상세히 보러가기<i class="m-icon-swapright m-icon-white"></i>
                </a>
            </div>
        </div>
    </li>
</c:forEach>