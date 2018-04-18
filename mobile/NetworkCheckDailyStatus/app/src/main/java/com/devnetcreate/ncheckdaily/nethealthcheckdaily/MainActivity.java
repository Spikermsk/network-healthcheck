package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import android.app.Fragment;
import android.os.Build;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.TextView;

import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;

import org.java_websocket.WebSocketImpl;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONException;
import org.json.JSONObject;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {



    private WebSocketClient mWebSocketClient;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        connectWebSocket();
    }

    private void connectWebSocket() {
        URI uri;
        try {
            uri = new URI("ws://echo.websocket.org/");
        } catch (URISyntaxException e) {
            e.printStackTrace();
            return;
        }

        mWebSocketClient = new WebSocketClient(uri) {
            @Override
            public void onOpen(ServerHandshake serverHandshake) {
                Log.i("Websocket", "Opened");
                mWebSocketClient.send("Hello from " + Build.MANUFACTURER + " " + Build.MODEL);
            }

            @Override
            public void onMessage(String s) {
                final String message = s;
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        try
                        {
                        JSONObject json = new JSONObject(message);

                            if(json.has("type") && json.has("data"))
                            {
                                Log.i("Websocket", json.getString("type"));

                                TextView textView = (TextView)findViewById(R.id.messages);
                                textView.setText(json.getString("data"));

                                //playerNum = Integer.parseInt(json.getString("data"));
                                Log.i("Websocket","Received... Type : " +json.getString("type")+" Data : "+json.getString("data"));
                            }
                        }
                        catch(JSONException e)
                        {
                        }


                    }
                });
            }

            @Override
            public void onClose(int i, String s, boolean b) {
                Log.i("Websocket", "Closed " + s);
            }

            @Override
            public void onError(Exception e) {
                Log.i("Websocket", "Error " + e.getMessage());
            }
        };
        mWebSocketClient.connect();
        WebSocketImpl.DEBUG = true;
    }

    public void sendMessage(View view) {
        EditText editText = (EditText)findViewById(R.id.message);
        mWebSocketClient.send(editText.getText().toString());
        editText.setText("");
    }
}
