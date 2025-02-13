import React, { useState, useEffect } from 'react';

function App() {
    const [transcript, setTranscript] = useState('');

    useEffect(() => {
        let websocket;
        let reconnectAttempts = 0;
        const maxReconnectAttempts = 5;

        const connect = () => {
            websocket = new WebSocket('ws://localhost:8765');

            websocket.onopen = () => {
                console.log("Connected to WebSocket server");
                reconnectAttempts = 0; // Reset reconnect counter
            };

            websocket.onmessage = (event) => {
                const newText = event.data;
                setTranscript(prev => prev + newText + " ");
            };

            websocket.onerror = (error) => {
                console.error("WebSocket error:", error);
            };

            websocket.onclose = (event) => {
                console.log("Disconnected - Code:", event.code, "Reason:", event.reason);

                if (reconnectAttempts < maxReconnectAttempts) {
                    const delay = Math.min(1000 * (2 ** reconnectAttempts), 10000);
                    console.log(`Reconnecting in ${delay}ms...`);
                    setTimeout(connect, delay);
                    reconnectAttempts++;
                }
            };
        };

        connect();

        return () => {
            if (websocket) websocket.close();
        };
    }, []);

    return (
        <div className="App">
            <h1>Real-time Transcription</h1>
            <div id="transcript">{transcript}</div>
        </div>
    );
}

export default App;