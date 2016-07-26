<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: gohyunyoung98
  Date: 16. 7. 25
  Time: 오후 5:19
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<c:forEach var="i" begin="10" end="20" step="1">
    <li class=timeline>
        <div class="timeline-time">
            <span class="time" style='color: #303a41'>${articleMap.get(String.valueOf(i)).date}</span>
        </div>
        <div class="timeline-icon">
        </div>
        <div class="timeline-body" data-name="${articleMap.get(String.valueOf(i)).emblem}">
            <h2>${articleMap.get(String.valueOf(i)).head}</h2>
            <div class="timeline-content">
                <img class="timeline-img pull-left" src=${String.format("/resources/images/emblem_image/emblemB_%s.png",articleMap.get(String.valueOf(i)).emblem)} alt="">
                    ${articleMap.get(String.valueOf(i)).intro}
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