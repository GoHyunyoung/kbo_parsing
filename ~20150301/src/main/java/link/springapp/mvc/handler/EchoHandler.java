package link.springapp.mvc.handler;

import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

/**
 * Created by yhhan on 15. 5. 6..
 */
public class EchoHandler extends TextWebSocketHandler {
    // 클라이언트에서 접속을 하여 성공할 경우 발생하는 이벤트
    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        super.afterConnectionEstablished(session);
        System.out.println("Session Connected");
    }

    // 클라이언트에서 send를 이용해서 메시지 발송을 한 경우 이벤트 핸들링
    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
        TextMessage echoMessage = new TextMessage("ECHO :" + message.getPayload());
        session.sendMessage(echoMessage);
    }

    // 클라이언트에서 연결을 종료할 경우 발생하는 이벤트
    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        super.afterConnectionClosed(session, status);
        System.out.println("Closed");
    }
}
