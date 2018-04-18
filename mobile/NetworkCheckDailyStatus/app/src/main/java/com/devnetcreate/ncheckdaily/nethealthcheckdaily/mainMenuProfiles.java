package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class mainMenuProfiles extends AppCompatActivity {

    Button btnCIO, btnDirector, btnManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu_profiles);

        btnCIO = findViewById(R.id.btnCIO);
        btnDirector = findViewById(R.id.btnDirector);
        btnManager = findViewById(R.id.btnManager);

        btnCIO.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(mainMenuProfiles.this, cio_health_activity.class);
                startActivity(i);
            }
        });

        btnDirector.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(mainMenuProfiles.this, director_ticket_status.class);
                startActivity(i);
            }
        });

        btnManager.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(mainMenuProfiles.this, manager_wan_avalability.class);
                startActivity(i);
            }
        });



    }
}
