import { useEffect, useState } from "react";
import axios from "axios";
import { Centrifuge, ConnectionTokenContext } from "centrifuge";
import { API_URL } from "./constants";

function App() {
  const [sid, setSid] = useState<string | null>(null);
  const [responseMessage, setResponseMessage] = useState<string>("");

  async function getAuthToken(ctx: ConnectionTokenContext): Promise<string> {
    const resp = await axios.get(`${API_URL}/token/auth`, {
      params: { user_id: 123 },
    });
    return resp.data;
  }

  async function getChannelToken(ctx: ConnectionTokenContext): Promise<string> {
    const resp = await axios.get(`${API_URL}/token/channel`, {
      params: { user_id: 123, channel: "general" },
    });
    return resp.data;
  }

  const centrifuge = new Centrifuge(
    "ws://localhost:8000/connection/websocket",
    {
      debug: true,
      getToken: getAuthToken,
    }
  );

  centrifuge.on("connected", function (ctx) {
    axios.post(`${API_URL}/sid/save`, { sid: ctx.client, user_id: 123 });
    console.log("connected", ctx);
  });

  centrifuge.on("disconnected", function (ctx) {
    console.log("disconnected", ctx);
  });

  const sub = centrifuge.newSubscription("general", {
    getToken: getChannelToken,
  });

  sub.on("subscribed", function (ctx) {
    console.log("subscribed", ctx);
  });

  sub.on("publication", function (ctx) {
    console.log("publication", ctx);
    setResponseMessage(ctx.data.text);
  });

  useEffect(() => {
    centrifuge.connect();
    sub.subscribe();
  }, []);

  return (
    <div>
      {responseMessage && (
        <div
          style={{
            marginTop: "20px",
            padding: "10px",
            backgroundColor: "#f0f0f0",
            borderRadius: "5px",
          }}
        >
          {responseMessage}
        </div>
      )}
    </div>
  );
}

export default App;
