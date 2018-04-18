package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.github.mikephil.charting.charts.PieChart;
import com.github.mikephil.charting.components.Description;
import com.github.mikephil.charting.components.Legend;
import com.github.mikephil.charting.data.PieData;
import com.github.mikephil.charting.data.PieDataSet;
import com.github.mikephil.charting.data.PieEntry;
import com.github.mikephil.charting.formatter.PercentFormatter;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class manager_wan_avalability extends AppCompatActivity {

    PieChart mChart;
    TextView tvTotal;
    String[] xData = { "up", "down"};
    float[] yJsonData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_manager_wan_avalability);

        APIInterface apiInterface;
        apiInterface = APIClient.getClient().create(APIInterface.class);

        Call<WanAvailability> call2 = apiInterface.getWanAvailability();
        call2.enqueue(new Callback<WanAvailability>() {
            @Override
            public void onResponse(Call<WanAvailability> call, Response<WanAvailability> response) {

                Log.d("TAG",response.code()+"");

                String displayResponse = "";

                WanAvailability resource = response.body();
                Integer up = Integer.parseInt(resource.up);
                Integer down = Integer.parseInt(resource.down);
                Integer total = Integer.parseInt(resource.total_time);

                try {
                    yJsonData = new float[2];
                    yJsonData[0] = up;
                    yJsonData[1] = down;

                } catch (Throwable tx) {
                    Log.e("My App", "Could not parse malformed JSON");
                }

                tvTotal = findViewById(R.id.txtTotal);
                tvTotal.setText("Total Time: " + total.toString());

                Log.d("TAG",displayResponse+"");

                mChart = findViewById(R.id.health_main);

                // configure pie chart
                mChart.setUsePercentValues(true);
                Description description = new Description();
                description.setTextColor(Color.BLACK);
                description.setText("Wan Availability");
                mChart.setDescription(description);

                // enable hole and configure
                mChart.setDrawHoleEnabled(true);
                //mChart.setHoleColorTransparent(true);
                mChart.setHoleRadius(7);
                mChart.setTransparentCircleRadius(10);

                // enable rotation of the chart by touch
                mChart.setRotationAngle(0);
                mChart.setRotationEnabled(true);

                //can set listeners for clicking on

                // add data
                addData();

                // customize legends
                Legend l = mChart.getLegend();
                l.setPosition(Legend.LegendPosition.RIGHT_OF_CHART);
                l.setXEntrySpace(7);
                l.setYEntrySpace(5);

            }

            @Override
            public void onFailure(Call<WanAvailability> call, Throwable t) {
                call.cancel();
            }
        });

    }

    private void addData() {
        ArrayList<PieEntry> yVals1 = new ArrayList<PieEntry>();

        for (int i = 0; i < yJsonData.length; i++)
            yVals1.add(new PieEntry(yJsonData[i], xData[i]));

        // create pie data set
        PieDataSet dataSet = new PieDataSet(yVals1, "Estados");
        dataSet.setSliceSpace(3);
        dataSet.setSelectionShift(5);

        final int[] MY_COLORS = { Color.rgb(0,255,0), Color.rgb(255,0,0),};
        ArrayList<Integer> colors = new ArrayList<Integer>();

        for(int c: MY_COLORS) colors.add(c);

        dataSet.setColors(colors);

        // instantiate pie data object now
        PieData data = new PieData(dataSet);
        data.setValueFormatter(new PercentFormatter());
        data.setValueTextSize(14f);
        data.setValueTextColor(Color.BLACK);

        mChart.setData(data);

        // undo all highlights
        mChart.highlightValues(null);

        // update pie chart
        mChart.invalidate();
        mChart.getLegend().setEnabled(false);
    }
}
