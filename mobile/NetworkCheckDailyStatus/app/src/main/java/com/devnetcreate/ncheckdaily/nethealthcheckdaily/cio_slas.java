package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.github.mikephil.charting.components.Description;
import com.github.mikephil.charting.components.Legend;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class cio_slas extends AppCompatActivity {

    TextView tv1, tv2, tv3, tv4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cio_slas);

        APIInterface apiInterface;
        apiInterface = APIClient.getClient().create(APIInterface.class);

        Call<Sla> call2 = apiInterface.getlas();
        call2.enqueue(new Callback<Sla>() {
            @Override
            public void onResponse(Call<Sla> call, Response<Sla> response) {

                Log.d("TAG",response.code()+"");

                String displayResponse = "";

                Sla resource = response.body();

                tv1 = findViewById(R.id.tvsla1);
                tv2 = findViewById(R.id.tvsla2);
                tv3 = findViewById(R.id.tvsla3);
                tv4 = findViewById(R.id.tvsla4);

                tv1.setText("Device Availability: " + resource.device_availability);
                tv2.setText("Up Time: " + resource.uptime);
                tv3.setText("Problems Detected: " + resource.problem_detected);
                tv4.setText("Critical Status: " + resource.critical_status);

                Log.d("TAG",displayResponse+"");

            }

            @Override
            public void onFailure(Call<Sla> call, Throwable t) {
                call.cancel();
            }
        });
    }
}
