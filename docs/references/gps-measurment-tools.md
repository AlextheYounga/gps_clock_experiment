Project Path: GNSSLogger

Source Tree:

```txt
GNSSLogger
├── app
│   ├── build.gradle
│   ├── libs
│   │   └── achartengine-1.2.0.jar
│   ├── proguard-rules.pro
│   └── src
│       ├── androidTest
│       │   └── java
│       │       └── com
│       │           └── google
│       │               └── android
│       │                   └── apps
│       │                       └── location
│       │                           └── gps
│       │                               └── gnsslogger
│       │                                   └── ExampleInstrumentedTest.java
│       ├── main
│       │   ├── AndroidManifest.xml
│       │   ├── ic_launcher-web.png
│       │   ├── java
│       │   │   └── com
│       │   │       └── google
│       │   │           └── android
│       │   │               └── apps
│       │   │                   └── location
│       │   │                       └── gps
│       │   │                           └── gnsslogger
│       │   │                               ├── AgnssFragment.java
│       │   │                               ├── AgnssUiLogger.java
│       │   │                               ├── DetectedActivitiesIntentReceiver.java
│       │   │                               ├── FileLogger.java
│       │   │                               ├── GroundTruthModeSwitcher.java
│       │   │                               ├── HelpDialog.java
│       │   │                               ├── LoggerFragment.java
│       │   │                               ├── MainActivity.java
│       │   │                               ├── MapFragment.java
│       │   │                               ├── MeasurementListener.java
│       │   │                               ├── MeasurementProvider.java
│       │   │                               ├── PlotFragment.java
│       │   │                               ├── RealTimePositionVelocityCalculator.java
│       │   │                               ├── ResultFragment.java
│       │   │                               ├── SettingsFragment.java
│       │   │                               ├── TimerFragment.java
│       │   │                               ├── TimerService.java
│       │   │                               ├── TimerValues.java
│       │   │                               └── UiLogger.java
│       │   └── res
│       │       ├── layout
│       │       │   ├── activity_main.xml
│       │       │   ├── fragment_agnss.xml
│       │       │   ├── fragment_log.xml
│       │       │   ├── fragment_main.xml
│       │       │   ├── fragment_plot.xml
│       │       │   ├── help.xml
│       │       │   ├── map_fragment.xml
│       │       │   ├── pop_up_window.xml
│       │       │   ├── results_log.xml
│       │       │   └── timer.xml
│       │       ├── mipmap-hdpi
│       │       │   └── ic_launcher.png
│       │       ├── mipmap-mdpi
│       │       │   └── ic_launcher.png
│       │       ├── mipmap-xhdpi
│       │       │   └── ic_launcher.png
│       │       ├── mipmap-xxhdpi
│       │       │   └── ic_launcher.png
│       │       ├── mipmap-xxxhdpi
│       │       │   └── ic_launcher.png
│       │       ├── raw
│       │       │   └── help_contents.txt
│       │       ├── values
│       │       │   ├── colors.xml
│       │       │   ├── dimens.xml
│       │       │   ├── strings.xml
│       │       │   └── styles.xml
│       │       ├── values-w820dp
│       │       │   └── dimens.xml
│       │       └── xml
│       │           └── file_providers_paths.xml
│       └── test
│           └── java
│               └── com
│                   └── google
│                       └── android
│                           └── apps
│                               └── location
│                                   └── gps
│                                       └── gnsslogger
│                                           └── ExampleUnitTest.java
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── gradlew.bat
├── local.defaults.properties
├── pseudorange
│   ├── build.gradle
│   ├── consumer-rules.pro
│   ├── libs
│   │   ├── asn1-base.jar
│   │   ├── asn1-supl2.jar
│   │   ├── commons-codec-1.10.jar
│   │   ├── commons-math3-3.6.1.jar
│   │   ├── protobuf-nano.jar
│   │   └── suplClient.jar
│   ├── proguard-rules.pro
│   └── src
│       ├── androidTest
│       │   └── java
│       │       └── com
│       │           └── google
│       │               └── android
│       │                   └── apps
│       │                       └── location
│       │                           └── gps
│       │                               └── gnsslogger
│       │                                   └── pseudorange
│       │                                       └── ExampleInstrumentedTest.java
│       ├── main
│       │   ├── AndroidManifest.xml
│       │   └── java
│       │       └── com
│       │           └── google
│       │               └── location
│       │                   └── lbs
│       │                       └── gnss
│       │                           └── gps
│       │                               └── pseudorange
│       │                                   ├── Ecef2EnuConverter.java
│       │                                   ├── Ecef2LlaConverter.java
│       │                                   ├── EcefToTopocentricConverter.java
│       │                                   ├── ElevationApiHelper.java
│       │                                   ├── GpsMathOperations.java
│       │                                   ├── GpsMeasurement.java
│       │                                   ├── GpsMeasurementWithRangeAndUncertainty.java
│       │                                   ├── GpsNavigationMessageStore.java
│       │                                   ├── GpsTime.java
│       │                                   ├── IonosphericModel.java
│       │                                   ├── Lla2EcefConverter.java
│       │                                   ├── PseudorangeNoSmoothingSmoother.java
│       │                                   ├── PseudorangePositionVelocityFromRealTimeEvents.java
│       │                                   ├── PseudorangeSmoother.java
│       │                                   ├── ResidualCorrectionCalculator.java
│       │                                   ├── SatelliteClockCorrectionCalculator.java
│       │                                   ├── SatellitePositionCalculator.java
│       │                                   ├── TroposphericModelEgnos.java
│       │                                   └── UserPositionVelocityWeightedLeastSquare.java
│       └── test
│           └── java
│               └── com
│                   └── google
│                       └── android
│                           └── apps
│                               └── location
│                                   └── gps
│                                       └── gnsslogger
│                                           └── pseudorange
│                                               └── ExampleUnitTest.java
└── settings.gradle

```

`app/build.gradle`:

```gradle
plugins {
    id 'com.android.application'
    id 'com.google.android.libraries.mapsplatform.secrets-gradle-plugin'
}

android {
    compileSdk 32

    defaultConfig {
        applicationId "com.google.android.apps.location.gps.gnsslogger"
        minSdk 24
        targetSdk 32
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {

    implementation 'androidx.appcompat:appcompat:1.4.2'
    implementation 'com.google.android.gms:play-services-location:20.0.0'
    implementation 'com.google.android.gms:play-services-maps:18.0.2'
    implementation 'androidx.localbroadcastmanager:localbroadcastmanager:1.1.0'
    implementation project(':pseudorange')
    implementation files('libs/achartengine-1.2.0.jar')
    implementation("com.google.guava:guava:31.1-android")
    implementation 'com.google.android.material:material:1.6.1'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    testImplementation 'junit:junit:4.13.2'
    implementation "androidx.core:core:1.8.0"
}


secrets {
    // To add your Maps API key to this project:
    // 1. Open the file local.properties found under the root project
    // 2. Add this line, where YOUR_API_KEY is your API key:
    //        MAPS_API_KEY=YOUR_API_KEY
    defaultPropertiesFileName 'local.defaults.properties'
}

```

`app/proguard-rules.pro`:

```pro
# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

# Uncomment this to preserve the line number information for
# debugging stack traces.
#-keepattributes SourceFile,LineNumberTable

# If you keep the line number information, uncomment this to
# hide the original source file name.
#-renamesourcefileattribute SourceFile
```

`app/src/androidTest/java/com/google/android/apps/location/gps/gnsslogger/ExampleInstrumentedTest.java`:

```java
package com.google.android.apps.location.gps.gnsslogger;

import static org.junit.Assert.*;

import android.content.Context;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.platform.app.InstrumentationRegistry;
import org.junit.Test;
import org.junit.runner.RunWith;

/**
 * Instrumented test, which will execute on an Android device.
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
@RunWith(AndroidJUnit4.class)
public class ExampleInstrumentedTest {
  @Test
  public void useAppContext() {
    // Context of the app under test.
    Context appContext = InstrumentationRegistry.getInstrumentation().getTargetContext();
    assertEquals("com.google.android.apps.location.gps.gnsslogger", appContext.getPackageName());
  }
}

```

`app/src/main/AndroidManifest.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.google.android.apps.location.gps.gnsslogger" >

    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS"/>
    <uses-permission android:name="com.google.android.gms.permission.ACTIVITY_RECOGNITION"/>
    <uses-permission android:name="com.google.android.providers.gsf.permission.READ_GSERVICES"/>
    <uses-permission android:name="com.google.android.providers.gsf.permission.WRITE_GSERVICES"/>
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme" >
        <meta-data
            android:name="com.google.android.gms.version"
            android:value="@integer/google_play_services_version" />
        <!-- Please add your own API key below -->
        <meta-data
            android:name="com.google.android.maps.v2.API_KEY"
            android:value="${MAPS_API_KEY}" />
        <activity
            android:name="com.google.android.apps.location.gps.gnsslogger.MainActivity"
            android:screenOrientation="portrait"
            android:alwaysRetainTaskState="true"
            android:label="@string/app_name"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <provider
            android:name="androidx.core.content.FileProvider"
            android:authorities="android.support.v4.provider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_providers_paths"/>
        </provider>
        <service android:name="com.google.android.apps.location.gps.gnsslogger.TimerService"
            android:exported="false"
            android:description="@string/timer_service_name" />
        <receiver
            android:name="com.google.android.apps.location.gps.gnsslogger.DetectedActivitiesIntentReceiver"
            android:exported="false" />
    </application>
</manifest>

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/AgnssFragment.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.app.Activity;
import android.content.Intent;
import android.location.LocationManager;
import android.os.Bundle;
import android.text.Editable;
import android.text.SpannableStringBuilder;
import android.text.style.ForegroundColorSpan;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ScrollView;
import android.widget.TextView;
import androidx.fragment.app.Fragment;

/** The UI fragment that hosts a logging view. */
public class AgnssFragment extends Fragment {

  public static final String TAG = ":AgnssFragment";
  private TextView mLogView;
  private ScrollView mScrollView;
  private MeasurementProvider mMeasurementProvider;
  private AgnssUiLogger mUiLogger;

  private final AgnssUIFragmentComponent mUiComponent = new AgnssUIFragmentComponent();

  public void setMeasurementProvider(MeasurementProvider value) {
    mMeasurementProvider = value;
  }

  public void setUILogger(AgnssUiLogger value) {
    mUiLogger = value;
  }

  @Override
  public View onCreateView(
      LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    View newView = inflater.inflate(R.layout.fragment_agnss, container, false /* attachToRoot */);
    mLogView = (TextView) newView.findViewById(R.id.log_view);
    mScrollView = (ScrollView) newView.findViewById(R.id.log_scroll);

    if (mUiLogger != null) {
      mUiLogger.setUiFragmentComponent(mUiComponent);
    }

    Button clearAgps = (Button) newView.findViewById(R.id.clearAgps);
    clearAgps.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            Log.i(MeasurementProvider.TAG + TAG, "Clearing AGPS");
            LocationManager locationManager = mMeasurementProvider.getLocationManager();
            locationManager.sendExtraCommand(
                LocationManager.GPS_PROVIDER, "delete_aiding_data", null);
            Log.i(MeasurementProvider.TAG + TAG, "Clearing AGPS command sent");
          }
        });

    Button fetchExtraData = (Button) newView.findViewById(R.id.fetchExtraData);
    fetchExtraData.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            Log.i(MeasurementProvider.TAG + TAG, "Fetching Extra data");
            LocationManager locationManager = mMeasurementProvider.getLocationManager();
            Bundle bundle = new Bundle();
            locationManager.sendExtraCommand("gps", "force_xtra_injection", bundle);
            Log.i(MeasurementProvider.TAG + TAG, "Fetching Extra data Command sent");
          }
        });

    Button fetchTimeData = (Button) newView.findViewById(R.id.fetchTimeData);
    fetchTimeData.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            Log.i(MeasurementProvider.TAG + TAG, "Fetching Time data");
            LocationManager locationManager = mMeasurementProvider.getLocationManager();
            Bundle bundle = new Bundle();
            locationManager.sendExtraCommand("gps", "force_time_injection", bundle);
            Log.i(MeasurementProvider.TAG + TAG, "Fetching Time data Command sent");
          }
        });

    Button requestSingleNlp = (Button) newView.findViewById(R.id.requestSingleNlp);
    requestSingleNlp.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            Log.i(MeasurementProvider.TAG + TAG, "Requesting Single NLP Location");
            mMeasurementProvider.registerSingleNetworkLocation();
            Log.i(MeasurementProvider.TAG + TAG, "Single NLP Location Requested");
          }
        });

    Button requestSingleGps = (Button) newView.findViewById(R.id.requestSingleGps);
    requestSingleGps.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            Log.i(MeasurementProvider.TAG + TAG, "Requesting Single GPS Location");
            mMeasurementProvider.registerSingleGpsLocation();
            Log.i(MeasurementProvider.TAG + TAG, "Single GPS Location Requested");
          }
        });
    Button clear = (Button) newView.findViewById(R.id.clear_log);
    clear.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            mLogView.setText("");
          }
        });

    return newView;
  }
  /** A facade for Agnss UI related operations. */
  public class AgnssUIFragmentComponent {

    private static final int MAX_LENGTH = 12000;
    private static final int LOWER_THRESHOLD = (int) (MAX_LENGTH * 0.5);

    public synchronized void logTextFragment(final String tag, final String text, int color) {
      final SpannableStringBuilder builder = new SpannableStringBuilder();
      builder.append(tag).append(" | ").append(text).append("\n");
      builder.setSpan(
          new ForegroundColorSpan(color),
          0 /* start */,
          builder.length(),
          SpannableStringBuilder.SPAN_INCLUSIVE_EXCLUSIVE);

      Activity activity = getActivity();
      if (activity == null) {
        return;
      }
      activity.runOnUiThread(
          new Runnable() {
            @Override
            public void run() {
              mLogView.append(builder);
              Editable editable = mLogView.getEditableText();
              int length = editable.length();
              if (length > MAX_LENGTH) {
                editable.delete(0, length - LOWER_THRESHOLD);
              }
            }
          });
    }

    public void startActivity(Intent intent) {
      getActivity().startActivity(intent);
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/AgnssUiLogger.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.graphics.Color;
import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.Location;
import android.os.Bundle;
import android.util.Log;
import com.google.android.apps.location.gps.gnsslogger.AgnssFragment.AgnssUIFragmentComponent;
import java.util.concurrent.TimeUnit;

/**
 * A class representing a UI logger for the application. Its responsibility is show information in
 * the UI.
 */
public class AgnssUiLogger implements MeasurementListener {

  private static final int USED_COLOR = Color.rgb(0x4a, 0x5f, 0x70);

  public AgnssUiLogger() {}

  private AgnssUIFragmentComponent mUiFragmentComponent;

  public synchronized AgnssUIFragmentComponent getUiFragmentComponent() {
    return mUiFragmentComponent;
  }

  public synchronized void setUiFragmentComponent(AgnssUIFragmentComponent value) {
    mUiFragmentComponent = value;
  }

  @Override
  public void onProviderEnabled(String provider) {
    logLocationEvent("onProviderEnabled: " + provider);
  }

  @Override
  public void onTTFFReceived(long l) {
    logLocationEvent("timeToFirstFix: " + TimeUnit.NANOSECONDS.toMillis(l) + "millis");
  }

  @Override
  public void onProviderDisabled(String provider) {
    logLocationEvent("onProviderDisabled: " + provider);
  }

  @Override
  public void onLocationChanged(Location location) {
    logLocationEvent("onLocationChanged: " + location);
  }

  @Override
  public void onLocationStatusChanged(String provider, int status, Bundle extras) {}

  @Override
  public void onGnssMeasurementsReceived(GnssMeasurementsEvent event) {}

  @Override
  public void onGnssMeasurementsStatusChanged(int status) {}

  @Override
  public void onGnssNavigationMessageReceived(GnssNavigationMessage event) {}

  @Override
  public void onGnssNavigationMessageStatusChanged(int status) {}

  @Override
  public void onGnssStatusChanged(GnssStatus gnssStatus) {}

  @Override
  public void onNmeaReceived(long timestamp, String s) {}

  @Override
  public void onListenerRegistration(String listener, boolean result) {
    logEvent("Registration", String.format("add%sListener: %b", listener, result), USED_COLOR);
  }

  private void logEvent(String tag, String message, int color) {
    String composedTag = MeasurementProvider.TAG + tag;
    Log.d(composedTag, message);
    logText(tag, message, color);
  }

  private void logText(String tag, String text, int color) {
    AgnssUIFragmentComponent component = getUiFragmentComponent();
    if (component != null) {
      component.logTextFragment(tag, text, color);
    }
  }

  private void logLocationEvent(String event) {
    logEvent("Location", event, USED_COLOR);
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/DetectedActivitiesIntentReceiver.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;

/**
 * A {@link BroadcastReceiver} that receives and broadcasts the result of {@link
 * com.google.android.gms.location.ActivityRecognition
 * #ActivityRecognitionApi#requestActivityUpdates()} to {@link MainActivity} to be further analyzed.
 */
public class DetectedActivitiesIntentReceiver extends BroadcastReceiver {
  public static String AR_RESULT_BROADCAST_ACTION =
      "com.google.android.apps.location.gps.gnsslogger.AR_RESULT_BROADCAST_ACTION";

  /**
   * Gets called when the result of {@link com.google.android.gms.location.ActivityRecognition
   * #ActivityRecognitionApi#requestActivityUpdates()} is available and handles incoming intents.
   *
   * @param intent The Intent is provided (inside a {@link android.app.PendingIntent}) when {@link
   *     com.google.android.gms.location.ActivityRecognition
   *     #ActivityRecognitionApi#requestActivityUpdates()} is called.
   */
  public void onReceive(Context context, Intent intent) {

    intent.setAction(AR_RESULT_BROADCAST_ACTION);
    LocalBroadcastManager.getInstance(context).sendBroadcast(intent);
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/FileLogger.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.content.Context;
import android.content.Intent;
import android.location.GnssClock;
import android.location.GnssMeasurement;
import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.Location;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.os.SystemClock;
import android.util.Log;
import android.widget.Toast;
import androidx.core.content.FileProvider;
import com.google.android.apps.location.gps.gnsslogger.LoggerFragment.UIFragmentComponent;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileFilter;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.Locale;

/** A GNSS logger to store information to a file. */
public class FileLogger implements MeasurementListener {

  private static final String TAG = "FileLogger";
  private static final String FILE_PREFIX = "gnss_log";
  private static final String ERROR_WRITING_FILE = "Problem writing to file.";
  private static final String COMMENT_START = "# ";
  private static final char RECORD_DELIMITER = ',';
  private static final String VERSION_TAG = "Version: ";

  private static final int MAX_FILES_STORED = 100;
  private static final int MINIMUM_USABLE_FILE_SIZE_BYTES = 1000;

  private final Context mContext;

  private final Object mFileLock = new Object();
  private BufferedWriter mFileWriter;
  private File mFile;

  private UIFragmentComponent mUiComponent;

  public synchronized UIFragmentComponent getUiComponent() {
    return mUiComponent;
  }

  public synchronized void setUiComponent(UIFragmentComponent value) {
    mUiComponent = value;
  }

  public FileLogger(Context context) {
    this.mContext = context;
  }

  /** Start a new file logging process. */
  public void startNewLog() {
    synchronized (mFileLock) {
      File baseDirectory;
      String state = Environment.getExternalStorageState();
      if (Environment.MEDIA_MOUNTED.equals(state)) {
        baseDirectory = new File(Environment.getExternalStorageDirectory(), FILE_PREFIX);
        baseDirectory.mkdirs();
      } else if (Environment.MEDIA_MOUNTED_READ_ONLY.equals(state)) {
        logError("Cannot write to external storage.");
        return;
      } else {
        logError("Cannot read external storage.");
        return;
      }

      SimpleDateFormat formatter = new SimpleDateFormat("yyy_MM_dd_HH_mm_ss");
      Date now = new Date();
      String fileName = String.format("%s_%s.txt", FILE_PREFIX, formatter.format(now));
      File currentFile = new File(baseDirectory, fileName);
      String currentFilePath = currentFile.getAbsolutePath();
      BufferedWriter currentFileWriter;
      try {
        currentFileWriter = new BufferedWriter(new FileWriter(currentFile));
      } catch (IOException e) {
        logException("Could not open file: " + currentFilePath, e);
        return;
      }

      // initialize the contents of the file
      try {
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.write("Header Description:");
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.write(VERSION_TAG);
        String manufacturer = Build.MANUFACTURER;
        String model = Build.MODEL;
        String fileVersion =
            mContext.getString(R.string.app_version)
                + " Platform: "
                + Build.VERSION.RELEASE
                + " "
                + "Manufacturer: "
                + manufacturer
                + " "
                + "Model: "
                + model;
        currentFileWriter.write(fileVersion);
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.write(
            "Raw,ElapsedRealtimeMillis,TimeNanos,LeapSecond,TimeUncertaintyNanos,FullBiasNanos,"
                + "BiasNanos,BiasUncertaintyNanos,DriftNanosPerSecond,DriftUncertaintyNanosPerSecond,"
                + "HardwareClockDiscontinuityCount,Svid,TimeOffsetNanos,State,ReceivedSvTimeNanos,"
                + "ReceivedSvTimeUncertaintyNanos,Cn0DbHz,PseudorangeRateMetersPerSecond,"
                + "PseudorangeRateUncertaintyMetersPerSecond,"
                + "AccumulatedDeltaRangeState,AccumulatedDeltaRangeMeters,"
                + "AccumulatedDeltaRangeUncertaintyMeters,CarrierFrequencyHz,CarrierCycles,"
                + "CarrierPhase,CarrierPhaseUncertainty,MultipathIndicator,SnrInDb,"
                + "ConstellationType,AgcDb");
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.write(
            "Fix,Provider,Latitude,Longitude,Altitude,Speed,Accuracy,(UTC)TimeInMs");
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.write("Nav,Svid,Type,Status,MessageId,Sub-messageId,Data(Bytes)");
        currentFileWriter.newLine();
        currentFileWriter.write(COMMENT_START);
        currentFileWriter.newLine();
      } catch (IOException e) {
        logException("Count not initialize file: " + currentFilePath, e);
        return;
      }

      if (mFileWriter != null) {
        try {
          mFileWriter.close();
        } catch (IOException e) {
          logException("Unable to close all file streams.", e);
          return;
        }
      }

      mFile = currentFile;
      mFileWriter = currentFileWriter;
      Toast.makeText(mContext, "File opened: " + currentFilePath, Toast.LENGTH_SHORT).show();

      // To make sure that files do not fill up the external storage:
      // - Remove all empty files
      FileFilter filter = new FileToDeleteFilter(mFile);
      for (File existingFile : baseDirectory.listFiles(filter)) {
        existingFile.delete();
      }
      // - Trim the number of files with data
      File[] existingFiles = baseDirectory.listFiles();
      int filesToDeleteCount = existingFiles.length - MAX_FILES_STORED;
      if (filesToDeleteCount > 0) {
        Arrays.sort(existingFiles);
        for (int i = 0; i < filesToDeleteCount; ++i) {
          existingFiles[i].delete();
        }
      }
    }
  }

  /**
   * Send the current log via email or other options selected from a pop menu shown to the user. A
   * new log is started when calling this function.
   */
  public void send() {
    if (mFile == null) {
      return;
    }

    Intent emailIntent = new Intent(Intent.ACTION_SEND);
    emailIntent.setType("*/*");
    emailIntent.putExtra(Intent.EXTRA_SUBJECT, "SensorLog");
    emailIntent.putExtra(Intent.EXTRA_TEXT, "");
    // attach the file
    Uri fileURI =
        FileProvider.getUriForFile(mContext, BuildConfig.APPLICATION_ID + ".provider", mFile);
    emailIntent.putExtra(Intent.EXTRA_STREAM, fileURI);
    getUiComponent().startActivity(Intent.createChooser(emailIntent, "Send log.."));
    if (mFileWriter != null) {
      try {
        mFileWriter.flush();
        mFileWriter.close();
        mFileWriter = null;
      } catch (IOException e) {
        logException("Unable to close all file streams.", e);
        return;
      }
    }
  }

  @Override
  public void onProviderEnabled(String provider) {}

  @Override
  public void onProviderDisabled(String provider) {}

  @Override
  public void onLocationChanged(Location location) {
    synchronized (mFileLock) {
      if (mFileWriter == null) {
        return;
      }
      String locationStream =
          String.format(
              Locale.US,
              "Fix,%s,%f,%f,%f,%f,%f,%d",
              location.getProvider(),
              location.getLatitude(),
              location.getLongitude(),
              location.getAltitude(),
              location.getSpeed(),
              location.getAccuracy(),
              location.getTime());
      try {
        mFileWriter.write(locationStream);
        mFileWriter.newLine();
      } catch (IOException e) {
        logException(ERROR_WRITING_FILE, e);
      }
    }
  }

  @Override
  public void onLocationStatusChanged(String provider, int status, Bundle extras) {}

  @Override
  public void onGnssMeasurementsReceived(GnssMeasurementsEvent event) {
    synchronized (mFileLock) {
      if (mFileWriter == null) {
        return;
      }
      GnssClock gnssClock = event.getClock();
      for (GnssMeasurement measurement : event.getMeasurements()) {
        try {
          writeGnssMeasurementToFile(gnssClock, measurement);
        } catch (IOException e) {
          logException(ERROR_WRITING_FILE, e);
        }
      }
    }
  }

  @Override
  public void onGnssMeasurementsStatusChanged(int status) {}

  @Override
  public void onGnssNavigationMessageReceived(GnssNavigationMessage navigationMessage) {
    synchronized (mFileLock) {
      if (mFileWriter == null) {
        return;
      }
      StringBuilder builder = new StringBuilder("Nav");
      builder.append(RECORD_DELIMITER);
      builder.append(navigationMessage.getSvid());
      builder.append(RECORD_DELIMITER);
      builder.append(navigationMessage.getType());
      builder.append(RECORD_DELIMITER);

      int status = navigationMessage.getStatus();
      builder.append(status);
      builder.append(RECORD_DELIMITER);
      builder.append(navigationMessage.getMessageId());
      builder.append(RECORD_DELIMITER);
      builder.append(navigationMessage.getSubmessageId());
      byte[] data = navigationMessage.getData();
      for (byte word : data) {
        builder.append(RECORD_DELIMITER);
        builder.append(word);
      }
      try {
        mFileWriter.write(builder.toString());
        mFileWriter.newLine();
      } catch (IOException e) {
        logException(ERROR_WRITING_FILE, e);
      }
    }
  }

  @Override
  public void onGnssNavigationMessageStatusChanged(int status) {}

  @Override
  public void onGnssStatusChanged(GnssStatus gnssStatus) {}

  @Override
  public void onNmeaReceived(long timestamp, String s) {
    synchronized (mFileLock) {
      if (mFileWriter == null) {
        return;
      }
      String nmeaStream = String.format(Locale.US, "NMEA,%s,%d", s.trim(), timestamp);
      try {
        mFileWriter.write(nmeaStream);
        mFileWriter.newLine();
      } catch (IOException e) {
        logException(ERROR_WRITING_FILE, e);
      }
    }
  }

  @Override
  public void onListenerRegistration(String listener, boolean result) {}

  @Override
  public void onTTFFReceived(long l) {}

  private void writeGnssMeasurementToFile(GnssClock clock, GnssMeasurement measurement)
      throws IOException {
    String clockStream =
        String.format(
            "Raw,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
            SystemClock.elapsedRealtime(),
            clock.getTimeNanos(),
            clock.hasLeapSecond() ? clock.getLeapSecond() : "",
            clock.hasTimeUncertaintyNanos() ? clock.getTimeUncertaintyNanos() : "",
            clock.getFullBiasNanos(),
            clock.hasBiasNanos() ? clock.getBiasNanos() : "",
            clock.hasBiasUncertaintyNanos() ? clock.getBiasUncertaintyNanos() : "",
            clock.hasDriftNanosPerSecond() ? clock.getDriftNanosPerSecond() : "",
            clock.hasDriftUncertaintyNanosPerSecond()
                ? clock.getDriftUncertaintyNanosPerSecond()
                : "",
            clock.getHardwareClockDiscontinuityCount() + ",");
    mFileWriter.write(clockStream);

    String measurementStream =
        String.format(
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
            measurement.getSvid(),
            measurement.getTimeOffsetNanos(),
            measurement.getState(),
            measurement.getReceivedSvTimeNanos(),
            measurement.getReceivedSvTimeUncertaintyNanos(),
            measurement.getCn0DbHz(),
            measurement.getPseudorangeRateMetersPerSecond(),
            measurement.getPseudorangeRateUncertaintyMetersPerSecond(),
            measurement.getAccumulatedDeltaRangeState(),
            measurement.getAccumulatedDeltaRangeMeters(),
            measurement.getAccumulatedDeltaRangeUncertaintyMeters(),
            measurement.hasCarrierFrequencyHz() ? measurement.getCarrierFrequencyHz() : "",
            measurement.hasCarrierCycles() ? measurement.getCarrierCycles() : "",
            measurement.hasCarrierPhase() ? measurement.getCarrierPhase() : "",
            measurement.hasCarrierPhaseUncertainty()
                ? measurement.getCarrierPhaseUncertainty()
                : "",
            measurement.getMultipathIndicator(),
            measurement.hasSnrInDb() ? measurement.getSnrInDb() : "",
            measurement.getConstellationType(),
            Build.VERSION.SDK_INT >= Build.VERSION_CODES.O
                    && measurement.hasAutomaticGainControlLevelDb()
                ? measurement.getAutomaticGainControlLevelDb()
                : "");
    mFileWriter.write(measurementStream);
    mFileWriter.newLine();
  }

  private void logException(String errorMessage, Exception e) {
    Log.e(MeasurementProvider.TAG + TAG, errorMessage, e);
    Toast.makeText(mContext, errorMessage, Toast.LENGTH_LONG).show();
  }

  private void logError(String errorMessage) {
    Log.e(MeasurementProvider.TAG + TAG, errorMessage);
    Toast.makeText(mContext, errorMessage, Toast.LENGTH_LONG).show();
  }

  /**
   * Implements a {@link FileFilter} to delete files that are not in the {@link
   * FileToDeleteFilter#mRetainedFiles}.
   */
  private static class FileToDeleteFilter implements FileFilter {
    private final List<File> mRetainedFiles;

    public FileToDeleteFilter(File... retainedFiles) {
      this.mRetainedFiles = Arrays.asList(retainedFiles);
    }

    /**
     * Returns {@code true} to delete the file, and {@code false} to keep the file.
     *
     * <p>Files are deleted if they are not in the {@link FileToDeleteFilter#mRetainedFiles} list.
     */
    @Override
    public boolean accept(File pathname) {
      if (pathname == null || !pathname.exists()) {
        return false;
      }
      if (mRetainedFiles.contains(pathname)) {
        return false;
      }
      return pathname.length() < MINIMUM_USABLE_FILE_SIZE_BYTES;
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/GroundTruthModeSwitcher.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

/** A class representing the interface toggling auto ground truth mode switch */
public interface GroundTruthModeSwitcher {
  /** Gets called to enable auto switch ground truth mode */
  void setAutoSwitchGroundTruthModeEnabled(boolean enabled);
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/HelpDialog.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.app.Dialog;
import android.content.Context;
import android.content.Intent;
import android.net.MailTo;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/** The Help Dialog of the Application */
public class HelpDialog extends Dialog {

  private static Context mContext = null;

  public HelpDialog(Context context) {
    super(context);
    mContext = context;
  }

  @Override
  public void onCreate(Bundle savedInstanceState) {
    setContentView(R.layout.help);
    WebView help = (WebView) findViewById(R.id.helpView);
    help.setWebViewClient(
        new WebViewClient() {
          @Override
          public boolean shouldOverrideUrlLoading(WebView view, String url) {
            if (url.startsWith("mailto:")) {
              MailTo mt = MailTo.parse(url);
              Intent emailIntent = new Intent(Intent.ACTION_SEND);
              emailIntent.setType("*/*");
              emailIntent.putExtra(Intent.EXTRA_SUBJECT, "GNSSLogger Feedback");
              emailIntent.putExtra(Intent.EXTRA_EMAIL, new String[] {mt.getTo()});
              emailIntent.putExtra(Intent.EXTRA_TEXT, "");
              mContext.startActivity(Intent.createChooser(emailIntent, "Send Feedback..."));
              return true;
            } else {
              view.loadUrl(url);
            }
            return true;
          }
        });

    String helpText = readRawTextFile(R.raw.help_contents);
    help.loadData(helpText, "text/html; charset=utf-8", "utf-8");
  }

  private String readRawTextFile(int id) {
    InputStream inputStream = mContext.getResources().openRawResource(id);
    InputStreamReader in = new InputStreamReader(inputStream);
    BufferedReader buf = new BufferedReader(in);
    String line;
    StringBuilder text = new StringBuilder();
    try {
      while ((line = buf.readLine()) != null) {
        text.append(line);
      }
    } catch (IOException e) {
      return null;
    }
    return text.toString();
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/LoggerFragment.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import static com.google.common.base.Preconditions.checkArgument;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.IBinder;
import android.preference.PreferenceManager;
import android.text.Editable;
import android.text.SpannableStringBuilder;
import android.text.style.ForegroundColorSpan;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.fragment.app.Fragment;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;
import com.google.android.apps.location.gps.gnsslogger.TimerService.TimerBinder;
import com.google.android.apps.location.gps.gnsslogger.TimerService.TimerListener;

/** The UI fragment that hosts a logging view. */
public class LoggerFragment extends Fragment implements TimerListener {
  private static final String TIMER_FRAGMENT_TAG = "timer";

  private TextView mLogView;
  private ScrollView mScrollView;
  private FileLogger mFileLogger;
  private UiLogger mUiLogger;
  private Button mStartLog;
  private Button mTimer;
  private Button mSendFile;
  private TextView mTimerDisplay;
  private TimerService mTimerService;
  private TimerValues mTimerValues =
      new TimerValues(0 /* hours */, 0 /* minutes */, 0 /* seconds */);
  private static boolean autoScroll = false;

  private final BroadcastReceiver mBroadcastReceiver =
      new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
          checkArgument(intent != null, "Intent is null");

          short intentType =
              intent.getByteExtra(TimerService.EXTRA_KEY_TYPE, TimerService.TYPE_UNKNOWN);

          // Be explicit in what types are handled here
          switch (intentType) {
            case TimerService.TYPE_UPDATE:
            case TimerService.TYPE_FINISH:
              break;
            default:
              return;
          }

          TimerValues countdown =
              new TimerValues(intent.getLongExtra(TimerService.EXTRA_KEY_UPDATE_REMAINING, 0L));
          LoggerFragment.this.displayTimer(countdown, true /* countdownStyle */);

          if (intentType == TimerService.TYPE_FINISH) {
            LoggerFragment.this.stopAndSend();
          }
        }
      };
  private ServiceConnection mConnection =
      new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName className, IBinder serviceBinder) {
          mTimerService = ((TimerBinder) serviceBinder).getService();
        }

        @Override
        public void onServiceDisconnected(ComponentName className) {
          mTimerService = null;
        }
      };

  private final UIFragmentComponent mUiComponent = new UIFragmentComponent();

  public void setUILogger(UiLogger value) {
    mUiLogger = value;
  }

  public void setFileLogger(FileLogger value) {
    mFileLogger = value;
  }

  @Override
  public void onResume() {
    super.onResume();
    LocalBroadcastManager.getInstance(getActivity())
        .registerReceiver(mBroadcastReceiver, new IntentFilter(TimerService.TIMER_ACTION));
  }

  @Override
  public void onPause() {
    LocalBroadcastManager.getInstance(getActivity()).unregisterReceiver(mBroadcastReceiver);
    super.onPause();
  }

  @Override
  public View onCreateView(
      LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    View newView = inflater.inflate(R.layout.fragment_log, container, false /* attachToRoot */);

    mLogView = (TextView) newView.findViewById(R.id.log_view);
    mScrollView = (ScrollView) newView.findViewById(R.id.log_scroll);

    getActivity()
        .bindService(
            new Intent(getActivity(), TimerService.class), mConnection, Context.BIND_AUTO_CREATE);

    UiLogger currentUiLogger = mUiLogger;
    if (currentUiLogger != null) {
      currentUiLogger.setUiFragmentComponent(mUiComponent);
    }
    FileLogger currentFileLogger = mFileLogger;
    if (currentFileLogger != null) {
      currentFileLogger.setUiComponent(mUiComponent);
    }

    Button start = (Button) newView.findViewById(R.id.start_log);
    Button end = (Button) newView.findViewById(R.id.end_log);
    Button clear = (Button) newView.findViewById(R.id.clear_log);

    start.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            mScrollView.fullScroll(View.FOCUS_UP);
          }
        });

    end.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            mScrollView.fullScroll(View.FOCUS_DOWN);
          }
        });

    clear.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            mLogView.setText("");
          }
        });

    mTimerDisplay = (TextView) newView.findViewById(R.id.timer_display);
    mTimer = (Button) newView.findViewById(R.id.timer);
    mStartLog = (Button) newView.findViewById(R.id.start_logs);
    mSendFile = (Button) newView.findViewById(R.id.send_file);

    displayTimer(mTimerValues, false /* countdownStyle */);
    enableOptions(true /* start */);

    mStartLog.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            enableOptions(false /* start */);
            Toast.makeText(getContext(), R.string.start_message, Toast.LENGTH_LONG).show();
            mFileLogger.startNewLog();

            if (!mTimerValues.isZero() && (mTimerService != null)) {
              mTimerService.startTimer();
            }
          }
        });

    mSendFile.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            stopAndSend();
          }
        });

    mTimer.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            launchTimerDialog();
          }
        });

    return newView;
  }

  void stopAndSend() {
    if (mTimer != null) {
      mTimerService.stopTimer();
    }
    enableOptions(true /* start */);
    Toast.makeText(getContext(), R.string.stop_message, Toast.LENGTH_LONG).show();
    displayTimer(mTimerValues, false /* countdownStyle */);
    mFileLogger.send();
  }

  void displayTimer(TimerValues values, boolean countdownStyle) {
    String content;

    if (countdownStyle) {
      content = values.toCountdownString();
    } else {
      content = values.toString();
    }

    mTimerDisplay.setText(
        String.format("%s: %s", getResources().getString(R.string.timer_display), content));
  }

  @Override
  public void processTimerValues(TimerValues values) {
    if (mTimerService != null) {
      mTimerService.setTimer(values);
    }
    mTimerValues = values;
    displayTimer(mTimerValues, false /* countdownStyle */);
  }

  private void launchTimerDialog() {
    TimerFragment timer = new TimerFragment();
    timer.setTargetFragment(this, 0);
    timer.setArguments(mTimerValues.toBundle());
    timer.show(getFragmentManager(), TIMER_FRAGMENT_TAG);
  }

  private void enableOptions(boolean start) {
    mTimer.setEnabled(start);
    mStartLog.setEnabled(start);
    mSendFile.setEnabled(!start);
  }

  /**
   * A facade for UI and Activity related operations that are required for {@link
   * MeasurementListener}s.
   */
  public class UIFragmentComponent {

    private static final int MAX_LENGTH = 42000;
    private static final int LOWER_THRESHOLD = (int) (MAX_LENGTH * 0.5);

    public synchronized void logTextFragment(final String tag, final String text, int color) {
      final SpannableStringBuilder builder = new SpannableStringBuilder();
      builder.append(tag).append(" | ").append(text).append("\n");
      builder.setSpan(
          new ForegroundColorSpan(color),
          0 /* start */,
          builder.length(),
          SpannableStringBuilder.SPAN_INCLUSIVE_EXCLUSIVE);

      Activity activity = getActivity();
      if (activity == null) {
        return;
      }
      activity.runOnUiThread(
          new Runnable() {
            @Override
            public void run() {
              mLogView.append(builder);
              SharedPreferences sharedPreferences =
                  PreferenceManager.getDefaultSharedPreferences(getActivity());
              Editable editable = mLogView.getEditableText();
              int length = editable.length();
              if (length > MAX_LENGTH) {
                editable.delete(0, length - LOWER_THRESHOLD);
              }
              if (sharedPreferences.getBoolean(
                  SettingsFragment.PREFERENCE_KEY_AUTO_SCROLL, false /*default return value*/)) {
                mScrollView.post(
                    new Runnable() {
                      @Override
                      public void run() {
                        mScrollView.fullScroll(View.FOCUS_DOWN);
                      }
                    });
              }
            }
          });
    }

    public void startActivity(Intent intent) {
      getActivity().startActivity(intent);
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/MainActivity.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;


import android.Manifest;
import android.app.Activity;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.os.IBinder;
import android.preference.PreferenceManager;
import android.util.Log;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentStatePagerAdapter;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;
import androidx.viewpager.widget.ViewPager;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.GoogleApiClient.ConnectionCallbacks;
import com.google.android.gms.common.api.GoogleApiClient.OnConnectionFailedListener;
import com.google.android.gms.location.ActivityRecognition;
import com.google.android.gms.location.ActivityRecognitionResult;
import com.google.android.gms.location.DetectedActivity;
import com.google.android.gms.location.LocationServices;
import com.google.android.material.tabs.TabLayout;
import java.util.Locale;

/** The activity for the application. */
public class MainActivity extends AppCompatActivity
    implements OnConnectionFailedListener, ConnectionCallbacks, GroundTruthModeSwitcher {
  private static final int LOCATION_REQUEST_ID = 1;
  private static final String[] REQUIRED_PERMISSIONS = {
    Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.WRITE_EXTERNAL_STORAGE
  };
  private static final int NUMBER_OF_FRAGMENTS = 6;
  private static final int FRAGMENT_INDEX_SETTING = 0;
  private static final int FRAGMENT_INDEX_LOGGER = 1;
  private static final int FRAGMENT_INDEX_RESULT = 2;
  private static final int FRAGMENT_INDEX_MAP = 3;
  private static final int FRAGMENT_INDEX_AGNSS = 4;
  private static final int FRAGMENT_INDEX_PLOT = 5;
  private static final String TAG = "MainActivity";

  private MeasurementProvider mMeasurementProvider;
  private UiLogger mUiLogger;
  private RealTimePositionVelocityCalculator mRealTimePositionVelocityCalculator;
  private FileLogger mFileLogger;
  private AgnssUiLogger mAgnssUiLogger;
  private Fragment[] mFragments;
  private GoogleApiClient mGoogleApiClient;
  private boolean mAutoSwitchGroundTruthMode;
  private final ActivityDetectionBroadcastReceiver mBroadcastReceiver =
      new ActivityDetectionBroadcastReceiver();

  private ServiceConnection mConnection =
      new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName className, IBinder serviceBinder) {
          // Empty
        }

        @Override
        public void onServiceDisconnected(ComponentName className) {
          // Empty
        }
      };

  @Override
  protected void onStart() {
    super.onStart();
    // Bind to the timer service to ensure it is available when app is running
    bindService(new Intent(this, TimerService.class), mConnection, Context.BIND_AUTO_CREATE);
  }

  @Override
  protected void onResume() {
    super.onResume();
    LocalBroadcastManager.getInstance(this)
        .registerReceiver(
            mBroadcastReceiver,
            new IntentFilter(DetectedActivitiesIntentReceiver.AR_RESULT_BROADCAST_ACTION));
  }

  @Override
  protected void onPause() {
    LocalBroadcastManager.getInstance(this).unregisterReceiver(mBroadcastReceiver);
    super.onPause();
  }

  @Override
  protected void onStop() {
    super.onStop();
    unbindService(mConnection);
  }

  @Override
  protected void onDestroy() {
    mMeasurementProvider.unregisterAll();
    super.onDestroy();
  }

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(this);
    SharedPreferences.Editor editor = sharedPreferences.edit();
    editor.putBoolean(SettingsFragment.PREFERENCE_KEY_AUTO_SCROLL, false);
    editor.commit();
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    buildGoogleApiClient();
    requestPermissionAndSetupFragments(this);
  }

  protected PendingIntent createActivityDetectionPendingIntent() {
    Intent intent = new Intent(this, DetectedActivitiesIntentReceiver.class);
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
      return PendingIntent.getBroadcast(this, 0, intent,
              PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_MUTABLE);
    } else {
      return PendingIntent.getBroadcast(this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
    }
  }

  private synchronized void buildGoogleApiClient() {
    mGoogleApiClient =
        new GoogleApiClient.Builder(this)
            .enableAutoManage(this, this)
            .addConnectionCallbacks(this)
            .addOnConnectionFailedListener(this)
            .addApi(ActivityRecognition.API)
            .addApi(LocationServices.API)
            .build();
  }

  @Override
  public void onConnectionFailed(@NonNull ConnectionResult result) {
    if (Log.isLoggable(TAG, Log.INFO)) {
      Log.i(TAG, "Connection failed: ErrorCode = " + result.getErrorCode());
    }
  }

  @Override
  public void onConnected(Bundle connectionHint) {
    if (Log.isLoggable(TAG, Log.INFO)) {
      Log.i(TAG, "Connected to GoogleApiClient");
    }
    try {
      ActivityRecognition.ActivityRecognitionApi.requestActivityUpdates(
          mGoogleApiClient, 0, createActivityDetectionPendingIntent());
    } catch (SecurityException e) {
      // TODO(adaext)
      //    ActivityCompat#requestPermissions
    }
  }

  @Override
  public void onConnectionSuspended(int cause) {
    if (Log.isLoggable(TAG, Log.INFO)) {
      Log.i(TAG, "Connection suspended");
    }
  }

  /**
   * A {@link FragmentPagerAdapter} that returns a fragment corresponding to one of the
   * sections/tabs/pages.
   */
  public class ViewPagerAdapter extends FragmentStatePagerAdapter {

    public ViewPagerAdapter(FragmentManager fm) {
      super(fm);
    }

    @Override
    public androidx.fragment.app.Fragment getItem(int position) {
      switch (position) {
        case FRAGMENT_INDEX_SETTING:
          return mFragments[FRAGMENT_INDEX_SETTING];
        case FRAGMENT_INDEX_LOGGER:
          return mFragments[FRAGMENT_INDEX_LOGGER];
        case FRAGMENT_INDEX_RESULT:
          return mFragments[FRAGMENT_INDEX_RESULT];
        case FRAGMENT_INDEX_MAP:
          return mFragments[FRAGMENT_INDEX_MAP];
        case FRAGMENT_INDEX_AGNSS:
          return mFragments[FRAGMENT_INDEX_AGNSS];
        case FRAGMENT_INDEX_PLOT:
          return mFragments[FRAGMENT_INDEX_PLOT];
        default:
          throw new IllegalArgumentException("Invalid section: " + position);
      }
    }

    @Override
    public int getCount() {
      // Show total pages.
      return NUMBER_OF_FRAGMENTS;
    }

    @Override
    public CharSequence getPageTitle(int position) {
      Locale locale = Locale.getDefault();
      switch (position) {
        case FRAGMENT_INDEX_SETTING:
          return getString(R.string.title_settings).toUpperCase(locale);
        case FRAGMENT_INDEX_LOGGER:
          return getString(R.string.title_log).toUpperCase(locale);
        case FRAGMENT_INDEX_RESULT:
          return getString(R.string.title_offset).toUpperCase(locale);
        case FRAGMENT_INDEX_MAP:
          return getString(R.string.title_map).toUpperCase(locale);
        case FRAGMENT_INDEX_AGNSS:
          return getString(R.string.title_agnss).toUpperCase(locale);
        case FRAGMENT_INDEX_PLOT:
          return getString(R.string.title_plot).toLowerCase(locale);
        default:
          return super.getPageTitle(position);
      }
    }
  }

  @Override
  public void onRequestPermissionsResult(
      int requestCode, String[] permissions, int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    if (requestCode == LOCATION_REQUEST_ID) {
      // If request is cancelled, the result arrays are empty.
      if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
        setupFragments();
      }
    }
  }

  private void setupFragments() {
    mUiLogger = new UiLogger();
    mRealTimePositionVelocityCalculator = new RealTimePositionVelocityCalculator();
    mRealTimePositionVelocityCalculator.setMainActivity(this);
    mRealTimePositionVelocityCalculator.setResidualPlotMode(
        RealTimePositionVelocityCalculator.RESIDUAL_MODE_DISABLED, null /* fixedGroundTruth */);

    mFileLogger = new FileLogger(getApplicationContext());
    mAgnssUiLogger = new AgnssUiLogger();
    mMeasurementProvider =
        new MeasurementProvider(
            getApplicationContext(),
            mGoogleApiClient,
            mUiLogger,
            mFileLogger,
            mRealTimePositionVelocityCalculator,
            mAgnssUiLogger);
    mFragments = new Fragment[NUMBER_OF_FRAGMENTS];
    SettingsFragment settingsFragment = new SettingsFragment();
    settingsFragment.setGpsContainer(mMeasurementProvider);
    settingsFragment.setRealTimePositionVelocityCalculator(mRealTimePositionVelocityCalculator);
    settingsFragment.setAutoModeSwitcher(this);
    mFragments[FRAGMENT_INDEX_SETTING] = settingsFragment;

    LoggerFragment loggerFragment = new LoggerFragment();
    loggerFragment.setUILogger(mUiLogger);
    loggerFragment.setFileLogger(mFileLogger);
    mFragments[FRAGMENT_INDEX_LOGGER] = loggerFragment;

    ResultFragment resultFragment = new ResultFragment();
    resultFragment.setPositionVelocityCalculator(mRealTimePositionVelocityCalculator);
    mFragments[FRAGMENT_INDEX_RESULT] = resultFragment;

    MapFragment mapFragment = new MapFragment();
    mapFragment.setPositionVelocityCalculator(mRealTimePositionVelocityCalculator);
    mFragments[FRAGMENT_INDEX_MAP] = mapFragment;

    AgnssFragment agnssFragment = new AgnssFragment();
    agnssFragment.setMeasurementProvider(mMeasurementProvider);
    agnssFragment.setUILogger(mAgnssUiLogger);
    mFragments[FRAGMENT_INDEX_AGNSS] = agnssFragment;

    PlotFragment plotFragment = new PlotFragment();
    mFragments[FRAGMENT_INDEX_PLOT] = plotFragment;
    mRealTimePositionVelocityCalculator.setPlotFragment(plotFragment);

    // The viewpager that will host the section contents.
    ViewPager viewPager = (ViewPager) findViewById(R.id.pager);
    viewPager.setOffscreenPageLimit(5);
    ViewPagerAdapter adapter = new ViewPagerAdapter(getSupportFragmentManager());
    viewPager.setAdapter(adapter);

    TabLayout tabLayout = (TabLayout) findViewById(R.id.tab_layout);
    tabLayout.setTabsFromPagerAdapter(adapter);

    // Set a listener via setOnTabSelectedListener(OnTabSelectedListener) to be notified when any
    // tab's selection state has been changed.
    tabLayout.setOnTabSelectedListener(new TabLayout.ViewPagerOnTabSelectedListener(viewPager));

    // Use a TabLayout.TabLayoutOnPageChangeListener to forward the scroll and selection changes to
    // this layout
    viewPager.addOnPageChangeListener(new TabLayout.TabLayoutOnPageChangeListener(tabLayout));
  }

  private boolean hasPermissions(Activity activity) {
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
      // Permissions granted at install time.
      return true;
    }
    for (String p : REQUIRED_PERMISSIONS) {
      if (ContextCompat.checkSelfPermission(activity, p) != PackageManager.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }

  private void requestPermissionAndSetupFragments(final Activity activity) {
    if (hasPermissions(activity)) {
      setupFragments();
    } else {
      ActivityCompat.requestPermissions(activity, REQUIRED_PERMISSIONS, LOCATION_REQUEST_ID);
    }
  }

  /** Toggles the flag to allow Activity Recognition updates to change ground truth mode */
  public void setAutoSwitchGroundTruthModeEnabled(boolean enabled) {
    mAutoSwitchGroundTruthMode = enabled;
  }

  /**
   * A receiver for result of {@link
   * ActivityRecognition#ActivityRecognitionApi#requestActivityUpdates()} broadcast by {@link
   * DetectedActivitiesIntentReceiver}
   */
  public class ActivityDetectionBroadcastReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {

      // Modify the status of mRealTimePositionVelocityCalculator only if the status is set to auto
      // (indicated by mAutoSwitchGroundTruthMode).
      if (mAutoSwitchGroundTruthMode) {
        ActivityRecognitionResult result = ActivityRecognitionResult.extractResult(intent);
        setGroundTruthModeOnResult(result);
      }
    }
  }

  /**
   * Sets up the ground truth mode of {@link RealTimePositionVelocityCalculator} given an result
   * from Activity Recognition update. For activities other than {@link DetectedActivity#STILL} and
   * {@link DetectedActivity#TILTING}, we conservatively assume the user is moving and use the last
   * WLS position solution as ground truth for corrected residual computation.
   */
  private void setGroundTruthModeOnResult(ActivityRecognitionResult result) {
    if (result != null) {
      int detectedActivityType = result.getMostProbableActivity().getType();
      if (detectedActivityType == DetectedActivity.STILL
          || detectedActivityType == DetectedActivity.TILTING) {
        mRealTimePositionVelocityCalculator.setResidualPlotMode(
            RealTimePositionVelocityCalculator.RESIDUAL_MODE_STILL, null);
      } else {
        mRealTimePositionVelocityCalculator.setResidualPlotMode(
            RealTimePositionVelocityCalculator.RESIDUAL_MODE_MOVING, null);
      }
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/MapFragment.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.fragment.app.Fragment;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapView;
import com.google.android.gms.maps.MapsInitializer;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

/**
 * A map fragment to show the computed least square position and the device computed position on
 * Google map.
 */
public class MapFragment extends Fragment implements OnMapReadyCallback {
  private static final float ZOOM_LEVEL = 15;
  private static final String TAG = "MapFragment";
  private RealTimePositionVelocityCalculator mPositionVelocityCalculator;

  private static final SimpleDateFormat DATE_SDF = new SimpleDateFormat("HH:mm:ss");

  // UI members
  private GoogleMap mMap; // Might be null if Google Play services APK is not available.
  private MapView mMapView;
  private final Set<Object> mSetOfFeatures = new HashSet<Object>();

  private Marker mLastLocationMarkerRaw = null;
  private Marker mLastLocationMarkerDevice = null;

  @Override
  public View onCreateView(
      LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    View rootView = inflater.inflate(R.layout.map_fragment, container, false);
    mMapView = ((MapView) rootView.findViewById(R.id.map));
    mMapView.onCreate(savedInstanceState);
    mMapView.getMapAsync(this);
    MapsInitializer.initialize(getActivity());

    RealTimePositionVelocityCalculator currentPositionVelocityCalculator =
        mPositionVelocityCalculator;
    if (currentPositionVelocityCalculator != null) {
      currentPositionVelocityCalculator.setMapFragment(this);
    }

    return rootView;
  }

  @Override
  public void onResume() {
    super.onResume();
    mMapView.onResume();
    if (mMap != null) {
      mMap.clear();
    }
    mLastLocationMarkerRaw = null;
    mLastLocationMarkerDevice = null;
  }

  @Override
  public void onPause() {
    mMapView.onPause();
    super.onPause();
  }

  @Override
  public void onDestroy() {
    mMapView.onDestroy();
    super.onDestroy();
  }

  @Override
  public void onMapReady(GoogleMap googleMap) {
    mMap = googleMap;
    try {
      mMap.setMyLocationEnabled(false);
    } catch (SecurityException e) {
      // TODO(adaext): implement the permission check properly.
      //    ActivityCompat#requestPermissions
      // here to request the missing permissions, and then overriding
      //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
      //                                          int[] grantResults)
      // to handle the case where the user grants the permission. See the documentation
      // for ActivityCompat#requestPermissions for more details.
    }
    mMap.getUiSettings().setZoomControlsEnabled(true);
    mMap.getUiSettings().setZoomGesturesEnabled(true);
    mMap.getUiSettings().setMapToolbarEnabled(false);
  }

  public void setPositionVelocityCalculator(RealTimePositionVelocityCalculator value) {
    mPositionVelocityCalculator = value;
  }

  public void updateMapViewWithPositions(
      final double latDegRaw,
      final double lngDegRaw,
      final double latDegDevice,
      final double lngDegDevice,
      final long timeMillis) {
    Activity activity = getActivity();
    if (activity == null) {
      return;
    }
    activity.runOnUiThread(
        new Runnable() {
          @Override
          public void run() {
            Log.i(TAG, "onLocationChanged");
            LatLng latLngRaw = new LatLng(latDegRaw, lngDegRaw);
            LatLng latLngDevice = new LatLng(latDegDevice, lngDegDevice);
            if (mLastLocationMarkerRaw == null && mLastLocationMarkerDevice == null) {
              if (mMap != null) {
                mLastLocationMarkerDevice =
                    mMap.addMarker(
                        new MarkerOptions()
                            .position(latLngDevice)
                            .title(getResources().getString(R.string.title_device))
                            .icon(
                                BitmapDescriptorFactory.defaultMarker(
                                    BitmapDescriptorFactory.HUE_BLUE)));
                mLastLocationMarkerDevice.showInfoWindow();

                mLastLocationMarkerRaw =
                    mMap.addMarker(
                        new MarkerOptions()
                            .position(latLngRaw)
                            .title(getResources().getString(R.string.title_wls))
                            .icon(
                                BitmapDescriptorFactory.defaultMarker(
                                    BitmapDescriptorFactory.HUE_GREEN)));
                mLastLocationMarkerRaw.showInfoWindow();

                mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(latLngRaw, ZOOM_LEVEL));
              }
            } else {
              mLastLocationMarkerRaw.setPosition(latLngRaw);
              mLastLocationMarkerDevice.setPosition(latLngDevice);
            }
            if (mLastLocationMarkerRaw == null && mLastLocationMarkerDevice == null) {
              String formattedDate = DATE_SDF.format(new Date(timeMillis));
              mLastLocationMarkerRaw.setTitle("time: " + formattedDate);
              mLastLocationMarkerDevice.showInfoWindow();

              mLastLocationMarkerRaw.setTitle("time: " + formattedDate);
              mLastLocationMarkerDevice.showInfoWindow();
            }
          }
        });
  }

  public void clearMarkers() {
    Activity activity = getActivity();
    if (activity == null) {
      return;
    }
    activity.runOnUiThread(
        new Runnable() {
          @Override
          public void run() {
            if (mLastLocationMarkerRaw != null) {
              mLastLocationMarkerRaw.remove();
              mLastLocationMarkerRaw = null;
            }
            if (mLastLocationMarkerDevice != null) {
              mLastLocationMarkerDevice.remove();
              mLastLocationMarkerDevice = null;
            }
          }
        });
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/MeasurementListener.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.Location;
import android.location.LocationListener;
import android.location.OnNmeaMessageListener;
import android.os.Bundle;

/** A class representing an interface for logging a measurement. */
public interface MeasurementListener {

  /** @see LocationListener#onProviderEnabled(String) */
  void onProviderEnabled(String provider);
  /** @see LocationListener#onProviderDisabled(String) */
  void onProviderDisabled(String provider);
  /** @see LocationListener#onLocationChanged(Location) */
  void onLocationChanged(Location location);
  /** @see LocationListener#onStatusChanged(String, int, Bundle) */
  void onLocationStatusChanged(String provider, int status, Bundle extras);
  /** @see GnssMeasurementsEvent.Callback# onGnssMeasurementsReceived(GnssMeasurementsEvent) */
  void onGnssMeasurementsReceived(GnssMeasurementsEvent event);
  /** @see GnssMeasurementsEvent.Callback#onStatusChanged(int) */
  void onGnssMeasurementsStatusChanged(int status);
  /** @see GnssNavigationMessage.Callback# onGnssNavigationMessageReceived(GnssNavigationMessage) */
  void onGnssNavigationMessageReceived(GnssNavigationMessage event);
  /** @see GnssNavigationMessage.Callback#onStatusChanged(int) */
  void onGnssNavigationMessageStatusChanged(int status);
  /** @see GnssStatus.Callback#onSatelliteStatusChanged(GnssStatus) */
  void onGnssStatusChanged(GnssStatus gnssStatus);
  /** Called when the listener is registered to listen to GNSS events */
  void onListenerRegistration(String listener, boolean result);
  /** @see OnNmeaMessageListener#onNmeaMessage(String, long) */
  void onNmeaReceived(long l, String s);

  void onTTFFReceived(long l);
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/MeasurementProvider.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.content.Context;
import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.Location;
import android.location.LocationManager;
import android.location.OnNmeaMessageListener;
import android.os.Bundle;
import android.os.SystemClock;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

/**
 * A container for measurement-related API calls. It binds the measurement providers with the
 * various {@link MeasurementListener} implementations.
 */
public class MeasurementProvider {

  public static final String TAG = "MeasurementProvider";

  private static final long LOCATION_RATE_GPS_MS = TimeUnit.SECONDS.toMillis(1L);
  private static final long LOCATION_RATE_NETWORK_MS = TimeUnit.SECONDS.toMillis(60L);

  private boolean mLogLocations = true;
  private boolean mLogNavigationMessages = true;
  private boolean mLogMeasurements = true;
  private boolean mLogStatuses = true;
  private boolean mLogNmeas = true;
  private long registrationTimeNanos = 0L;
  private long firstLocationTimeNanos = 0L;
  private long ttff = 0L;
  private boolean firstTime = true;

  GoogleApiClient mGoogleApiClient;
  private final List<MeasurementListener> mListeners;

  private final LocationManager mLocationManager;
  private final android.location.LocationListener mLocationListener =
      new android.location.LocationListener() {

        @Override
        public void onProviderEnabled(String provider) {
          if (mLogLocations) {
            for (MeasurementListener listener : mListeners) {
              if (listener instanceof AgnssUiLogger && !firstTime) {
                continue;
              }
              listener.onProviderEnabled(provider);
            }
          }
        }

        @Override
        public void onProviderDisabled(String provider) {
          if (mLogLocations) {
            for (MeasurementListener logger : mListeners) {
              if (logger instanceof AgnssUiLogger && !firstTime) {
                continue;
              }
              logger.onProviderDisabled(provider);
            }
          }
        }

        @Override
        public void onLocationChanged(Location location) {
          if (firstTime && location.getProvider().equals(LocationManager.GPS_PROVIDER)) {
            if (mLogLocations) {
              for (MeasurementListener logger : mListeners) {
                firstLocationTimeNanos = SystemClock.elapsedRealtimeNanos();
                ttff = firstLocationTimeNanos - registrationTimeNanos;
                logger.onTTFFReceived(ttff);
              }
            }
            firstTime = false;
          }
          if (mLogLocations) {
            for (MeasurementListener logger : mListeners) {
              if (logger instanceof AgnssUiLogger && !firstTime) {
                continue;
              }
              logger.onLocationChanged(location);
            }
          }
        }

        @Override
        public void onStatusChanged(String provider, int status, Bundle extras) {
          if (mLogLocations) {
            for (MeasurementListener logger : mListeners) {
              logger.onLocationStatusChanged(provider, status, extras);
            }
          }
        }
      };

  private final com.google.android.gms.location.LocationListener mFusedLocationListener =
      new com.google.android.gms.location.LocationListener() {

        @Override
        public void onLocationChanged(Location location) {
          if (firstTime && location.getProvider().equals(LocationManager.GPS_PROVIDER)) {
            if (mLogLocations) {
              for (MeasurementListener logger : mListeners) {
                firstLocationTimeNanos = SystemClock.elapsedRealtimeNanos();
                ttff = firstLocationTimeNanos - registrationTimeNanos;
                logger.onTTFFReceived(ttff);
              }
            }
            firstTime = false;
          }
          if (mLogLocations) {
            for (MeasurementListener logger : mListeners) {
              if (logger instanceof AgnssUiLogger && !firstTime) {
                continue;
              }
              logger.onLocationChanged(location);
            }
          }
        }
      };

  private final GnssMeasurementsEvent.Callback gnssMeasurementsEventListener =
      new GnssMeasurementsEvent.Callback() {
        @Override
        public void onGnssMeasurementsReceived(GnssMeasurementsEvent event) {
          if (mLogMeasurements) {
            for (MeasurementListener logger : mListeners) {
              logger.onGnssMeasurementsReceived(event);
            }
          }
        }

        @Override
        public void onStatusChanged(int status) {
          if (mLogMeasurements) {
            for (MeasurementListener logger : mListeners) {
              logger.onGnssMeasurementsStatusChanged(status);
            }
          }
        }
      };

  private final GnssNavigationMessage.Callback gnssNavigationMessageListener =
      new GnssNavigationMessage.Callback() {
        @Override
        public void onGnssNavigationMessageReceived(GnssNavigationMessage event) {
          if (mLogNavigationMessages) {
            for (MeasurementListener logger : mListeners) {
              logger.onGnssNavigationMessageReceived(event);
            }
          }
        }

        @Override
        public void onStatusChanged(int status) {
          if (mLogNavigationMessages) {
            for (MeasurementListener logger : mListeners) {
              logger.onGnssNavigationMessageStatusChanged(status);
            }
          }
        }
      };

  private final GnssStatus.Callback gnssStatusListener =
      new GnssStatus.Callback() {
        @Override
        public void onStarted() {}

        @Override
        public void onStopped() {}

        @Override
        public void onFirstFix(int ttff) {}

        @Override
        public void onSatelliteStatusChanged(GnssStatus status) {
          for (MeasurementListener logger : mListeners) {
            logger.onGnssStatusChanged(status);
          }
        }
      };

  private final OnNmeaMessageListener nmeaListener =
      new OnNmeaMessageListener() {
        @Override
        public void onNmeaMessage(String s, long l) {
          if (mLogNmeas) {
            for (MeasurementListener logger : mListeners) {
              logger.onNmeaReceived(l, s);
            }
          }
        }
      };

  public MeasurementProvider(
      Context context, GoogleApiClient client, MeasurementListener... loggers) {
    this.mListeners = Arrays.asList(loggers);
    mLocationManager = (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);
    this.mGoogleApiClient = client;
  }

  public LocationManager getLocationManager() {
    return mLocationManager;
  }

  public void setLogLocations(boolean value) {
    mLogLocations = value;
  }

  public boolean canLogLocations() {
    return mLogLocations;
  }

  public void setLogNavigationMessages(boolean value) {
    mLogNavigationMessages = value;
  }

  public boolean canLogNavigationMessages() {
    return mLogNavigationMessages;
  }

  public void setLogMeasurements(boolean value) {
    mLogMeasurements = value;
  }

  public boolean canLogMeasurements() {
    return mLogMeasurements;
  }

  public void setLogStatuses(boolean value) {
    mLogStatuses = value;
  }

  public boolean canLogStatuses() {
    return mLogStatuses;
  }

  public void setLogNmeas(boolean value) {
    mLogNmeas = value;
  }

  public boolean canLogNmeas() {
    return mLogNmeas;
  }

  public void registerLocation() {
    boolean isGpsProviderEnabled = mLocationManager.isProviderEnabled(LocationManager.GPS_PROVIDER);
    if (isGpsProviderEnabled) {
      try {
        mLocationManager.requestLocationUpdates(
            LocationManager.NETWORK_PROVIDER,
            LOCATION_RATE_NETWORK_MS,
            0.0f /* minDistance */,
            mLocationListener);
        mLocationManager.requestLocationUpdates(
            LocationManager.GPS_PROVIDER,
            LOCATION_RATE_GPS_MS,
            0.0f /* minDistance */,
            mLocationListener);
      } catch (SecurityException e) {
        // TODO(adaext)
        //    ActivityCompat#requestPermissions
        // here to request the missing permissions, and then overriding
        //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
        //                                          int[] grantResults)
        // to handle the case where the user grants the permission. See the documentation
        // for ActivityCompat#requestPermissions for more details.
      }
    }
    logRegistration("LocationUpdates", isGpsProviderEnabled);
  }

  public void unregisterLocation() {
    mLocationManager.removeUpdates(mLocationListener);
  }

  public void registerFusedLocation() {
    LocationRequest locationRequest = new LocationRequest();
    locationRequest.setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY);
    locationRequest.setInterval(1000);
    locationRequest.setFastestInterval(100);
    try {
      LocationServices.FusedLocationApi.requestLocationUpdates(
          mGoogleApiClient, locationRequest, mFusedLocationListener);
    } catch (SecurityException e) {
      // TODO(adaext):
      //    ActivityCompat#requestPermissions
      // here to request the missing permissions, and then overriding
      //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
      //                                          int[] grantResults)
      // to handle the case where the user grants the permission. See the documentation
      // for ActivityCompat#requestPermissions for more details.
    }
  }

  public void unRegisterFusedLocation() {
    if (mGoogleApiClient != null) {
      LocationServices.FusedLocationApi.removeLocationUpdates(
          mGoogleApiClient, mFusedLocationListener);
    }
  }

  public void registerSingleNetworkLocation() {
    boolean isNetworkProviderEnabled =
        mLocationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER);
    if (isNetworkProviderEnabled) {
      try {
        mLocationManager.requestSingleUpdate(
            LocationManager.NETWORK_PROVIDER, mLocationListener, null);
      } catch (SecurityException e) {
        // TODO(adaext):
        //    ActivityCompat#requestPermissions
        // here to request the missing permissions, and then overriding
        //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
        //                                          int[] grantResults)
        // to handle the case where the user grants the permission. See the documentation
        // for ActivityCompat#requestPermissions for more details.
      }
    }
    logRegistration("LocationUpdates", isNetworkProviderEnabled);
  }

  public void registerSingleGpsLocation() {
    boolean isGpsProviderEnabled = mLocationManager.isProviderEnabled(LocationManager.GPS_PROVIDER);
    if (isGpsProviderEnabled) {
      this.firstTime = true;
      registrationTimeNanos = SystemClock.elapsedRealtimeNanos();
      try {
        mLocationManager.requestSingleUpdate(LocationManager.GPS_PROVIDER, mLocationListener, null);
      } catch (SecurityException e) {
        // TODO(adaext):
        //    ActivityCompat#requestPermissions
        // here to request the missing permissions, and then overriding
        //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
        //                                          int[] grantResults)
        // to handle the case where the user grants the permission. See the documentation
        // for ActivityCompat#requestPermissions for more details.
      }
    }
    logRegistration("LocationUpdates", isGpsProviderEnabled);
  }

  public void registerMeasurements() {
    try {
      logRegistration(
          "GnssMeasurements",
          mLocationManager.registerGnssMeasurementsCallback(gnssMeasurementsEventListener));
    } catch (SecurityException e) {
      // TODO(adaext):
      //    ActivityCompat#requestPermissions
      // here to request the missing permissions, and then overriding
      //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
      //                                          int[] grantResults)
      // to handle the case where the user grants the permission. See the documentation
      // for ActivityCompat#requestPermissions for more details.
    }
  }

  public void unregisterMeasurements() {
    mLocationManager.unregisterGnssMeasurementsCallback(gnssMeasurementsEventListener);
  }

  public void registerNavigation() {
    logRegistration(
        "GpsNavigationMessage",
        mLocationManager.registerGnssNavigationMessageCallback(gnssNavigationMessageListener));
  }

  public void unregisterNavigation() {
    mLocationManager.unregisterGnssNavigationMessageCallback(gnssNavigationMessageListener);
  }

  public void registerGnssStatus() {
    try {
      logRegistration(
          "GnssStatus", mLocationManager.registerGnssStatusCallback(gnssStatusListener));
    } catch (SecurityException e) {
      // TODO(adaext):
      //    ActivityCompat#requestPermissions
      // here to request the missing permissions, and then overriding
      //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
      //                                          int[] grantResults)
      // to handle the case where the user grants the permission. See the documentation
      // for ActivityCompat#requestPermissions for more details.
    }
  }

  public void unregisterGpsStatus() {
    mLocationManager.unregisterGnssStatusCallback(gnssStatusListener);
  }

  public void registerNmea() {
    try {
      logRegistration("Nmea", mLocationManager.addNmeaListener(nmeaListener));
    } catch (SecurityException e) {
      // TODO(adaext):
      //    ActivityCompat#requestPermissions
      // here to request the missing permissions, and then overriding
      //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
      //                                          int[] grantResults)
      // to handle the case where the user grants the permission. See the documentation
      // for ActivityCompat#requestPermissions for more details.
    }
  }

  public void unregisterNmea() {
    mLocationManager.removeNmeaListener(nmeaListener);
  }

  public void registerAll() {
    registerLocation();
    registerMeasurements();
    registerNavigation();
    registerGnssStatus();
    registerNmea();
  }

  public void unregisterAll() {
    unregisterLocation();
    unregisterMeasurements();
    unregisterNavigation();
    unregisterGpsStatus();
    unregisterNmea();
  }

  private void logRegistration(String listener, boolean result) {
    for (MeasurementListener logger : mListeners) {
      if (logger instanceof AgnssUiLogger && !firstTime) {
        continue;
      }
      logger.onListenerRegistration(listener, result);
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/PlotFragment.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.content.Context;
import android.graphics.Color;
import android.graphics.Paint.Align;
import android.location.GnssMeasurement;
import android.location.GnssMeasurementsEvent;
import android.location.GnssStatus;
import android.os.Bundle;
import android.text.Spannable;
import android.text.SpannableStringBuilder;
import android.text.style.ForegroundColorSpan;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemSelectedListener;
import android.widget.LinearLayout;
import android.widget.Spinner;
import android.widget.TextView;
import androidx.collection.ArrayMap;
import androidx.fragment.app.Fragment;
import com.google.location.lbs.gnss.gps.pseudorange.GpsNavigationMessageStore;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.achartengine.ChartFactory;
import org.achartengine.GraphicalView;
import org.achartengine.model.XYMultipleSeriesDataset;
import org.achartengine.model.XYSeries;
import org.achartengine.renderer.XYMultipleSeriesRenderer;
import org.achartengine.renderer.XYSeriesRenderer;
import org.achartengine.util.MathHelper;

/** A plot fragment to show real-time Gnss analysis migrated from GnssAnalysis Tool. */
public class PlotFragment extends Fragment {

  /** Total number of kinds of plot tabs */
  private static final int NUMBER_OF_TABS = 2;

  /** The position of the CN0 over time plot tab */
  private static final int CN0_TAB = 0;

  /** The position of the prearrange residual plot tab */
  private static final int PR_RESIDUAL_TAB = 1;

  /** The number of Gnss constellations */
  private static final int NUMBER_OF_CONSTELLATIONS = 6;

  /** The X range of the plot, we are keeping the latest one minute visible */
  private static final double TIME_INTERVAL_SECONDS = 60;

  /** The index in data set we reserved for the plot containing all constellations */
  private static final int DATA_SET_INDEX_ALL = 0;

  /** The number of satellites we pick for the strongest satellite signal strength calculation */
  private static final int NUMBER_OF_STRONGEST_SATELLITES = 4;

  /** Data format used to format the data in the text view */
  private static final DecimalFormat sDataFormat =
      new DecimalFormat("##.#", new DecimalFormatSymbols(Locale.US));

  private GraphicalView mChartView;

  /** The average of the average of strongest satellite signal strength over history */
  private double mAverageCn0 = 0;

  /** Total number of {@link GnssMeasurementsEvent} has been received */
  private int mMeasurementCount = 0;

  private double mInitialTimeSeconds = -1;
  private TextView mAnalysisView;
  private double mLastTimeReceivedSeconds = 0;
  private final ColorMap mColorMap = new ColorMap();
  private DataSetManager mDataSetManager;
  private XYMultipleSeriesRenderer mCurrentRenderer;
  private LinearLayout mLayout;
  private int mCurrentTab = 0;

  @Override
  public View onCreateView(
      LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    View plotView = inflater.inflate(R.layout.fragment_plot, container, false /* attachToRoot */);

    mDataSetManager =
        new DataSetManager(NUMBER_OF_TABS, NUMBER_OF_CONSTELLATIONS, getContext(), mColorMap);

    // Set UI elements handlers
    final Spinner spinner = plotView.findViewById(R.id.constellation_spinner);
    final Spinner tabSpinner = plotView.findViewById(R.id.tab_spinner);

    OnItemSelectedListener spinnerOnSelectedListener =
        new OnItemSelectedListener() {

          @Override
          public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
            mCurrentTab = tabSpinner.getSelectedItemPosition();
            XYMultipleSeriesRenderer renderer =
                mDataSetManager.getRenderer(mCurrentTab, spinner.getSelectedItemPosition());
            XYMultipleSeriesDataset dataSet =
                mDataSetManager.getDataSet(mCurrentTab, spinner.getSelectedItemPosition());
            if (mLastTimeReceivedSeconds > TIME_INTERVAL_SECONDS) {
              renderer.setXAxisMax(mLastTimeReceivedSeconds);
              renderer.setXAxisMin(mLastTimeReceivedSeconds - TIME_INTERVAL_SECONDS);
            }
            mCurrentRenderer = renderer;
            mLayout.removeAllViews();
            mChartView = ChartFactory.getLineChartView(getContext(), dataSet, renderer);
            mLayout.addView(mChartView);
          }

          @Override
          public void onNothingSelected(AdapterView<?> parent) {}
        };

    spinner.setOnItemSelectedListener(spinnerOnSelectedListener);
    tabSpinner.setOnItemSelectedListener(spinnerOnSelectedListener);

    // Set up the Graph View
    mCurrentRenderer = mDataSetManager.getRenderer(mCurrentTab, DATA_SET_INDEX_ALL);
    XYMultipleSeriesDataset currentDataSet =
        mDataSetManager.getDataSet(mCurrentTab, DATA_SET_INDEX_ALL);
    mChartView = ChartFactory.getLineChartView(getContext(), currentDataSet, mCurrentRenderer);
    mAnalysisView = plotView.findViewById(R.id.analysis);
    mAnalysisView.setTextColor(Color.BLACK);
    mLayout = plotView.findViewById(R.id.plot);
    mLayout.addView(mChartView);
    return plotView;
  }

  /** Updates the CN0 versus Time plot data from a {@link GnssMeasurement} */
  protected void updateCnoTab(GnssMeasurementsEvent event) {
    long timeInSeconds = TimeUnit.NANOSECONDS.toSeconds(event.getClock().getTimeNanos());
    if (mInitialTimeSeconds < 0) {
      mInitialTimeSeconds = timeInSeconds;
    }

    // Building the texts message in analysis text view
    List<GnssMeasurement> measurements =
        sortByCarrierToNoiseRatio(new ArrayList<>(event.getMeasurements()));
    SpannableStringBuilder builder = new SpannableStringBuilder();
    double currentAverage = 0;
    if (measurements.size() >= NUMBER_OF_STRONGEST_SATELLITES) {
      mAverageCn0 =
          (mAverageCn0 * mMeasurementCount
                  + (measurements.get(0).getCn0DbHz()
                          + measurements.get(1).getCn0DbHz()
                          + measurements.get(2).getCn0DbHz()
                          + measurements.get(3).getCn0DbHz())
                      / NUMBER_OF_STRONGEST_SATELLITES)
              / (++mMeasurementCount);
      currentAverage =
          (measurements.get(0).getCn0DbHz()
                  + measurements.get(1).getCn0DbHz()
                  + measurements.get(2).getCn0DbHz()
                  + measurements.get(3).getCn0DbHz())
              / NUMBER_OF_STRONGEST_SATELLITES;
    }
    builder.append(
        getString(R.string.history_average_hint, sDataFormat.format(mAverageCn0) + "\n"));
    builder.append(
        getString(R.string.current_average_hint, sDataFormat.format(currentAverage) + "\n"));
    for (int i = 0; i < NUMBER_OF_STRONGEST_SATELLITES && i < measurements.size(); i++) {
      int start = builder.length();
      builder.append(
          mDataSetManager.getConstellationPrefix(measurements.get(i).getConstellationType())
              + measurements.get(i).getSvid()
              + ": "
              + sDataFormat.format(measurements.get(i).getCn0DbHz())
              + "\n");
      int end = builder.length();
      builder.setSpan(
          new ForegroundColorSpan(
              mColorMap.getColor(
                  measurements.get(i).getSvid(), measurements.get(i).getConstellationType())),
          start,
          end,
          Spannable.SPAN_INCLUSIVE_EXCLUSIVE);
    }
    builder.append(getString(R.string.satellite_number_sum_hint, measurements.size()));
    mAnalysisView.setText(builder);

    // Adding incoming data into Dataset
    mLastTimeReceivedSeconds = timeInSeconds - mInitialTimeSeconds;
    for (GnssMeasurement measurement : measurements) {
      int constellationType = measurement.getConstellationType();
      int svID = measurement.getSvid();
      if (constellationType != GnssStatus.CONSTELLATION_UNKNOWN) {
        mDataSetManager.addValue(
            CN0_TAB, constellationType, svID, mLastTimeReceivedSeconds, measurement.getCn0DbHz());
      }
    }

    mDataSetManager.fillInDiscontinuity(CN0_TAB, mLastTimeReceivedSeconds);

    // Checks if the plot has reached the end of frame and resize
    if (mLastTimeReceivedSeconds > mCurrentRenderer.getXAxisMax()) {
      mCurrentRenderer.setXAxisMax(mLastTimeReceivedSeconds);
      mCurrentRenderer.setXAxisMin(mLastTimeReceivedSeconds - TIME_INTERVAL_SECONDS);
    }

    mChartView.invalidate();
  }

  /**
   * Updates the pseudorange residual plot from residual results calculated by {@link
   * RealTimePositionVelocityCalculator}
   *
   * @param residuals An array of MAX_NUMBER_OF_SATELLITES elements where indexes of satellites was
   *     not seen are fixed with {@code Double.NaN} and indexes of satellites what were seen are
   *     filled with pseudorange residual in meters
   * @param timeInSeconds the time at which measurements are received
   */
  protected void updatePseudorangeResidualTab(double[] residuals, double timeInSeconds) {
    double timeSinceLastMeasurement = timeInSeconds - mInitialTimeSeconds;
    for (int i = 1; i <= GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES; i++) {
      if (!Double.isNaN(residuals[i - 1])) {
        mDataSetManager.addValue(
            PR_RESIDUAL_TAB,
            GnssStatus.CONSTELLATION_GPS,
            i,
            timeSinceLastMeasurement,
            residuals[i - 1]);
      }
    }
    mDataSetManager.fillInDiscontinuity(PR_RESIDUAL_TAB, timeSinceLastMeasurement);
  }

  private List<GnssMeasurement> sortByCarrierToNoiseRatio(List<GnssMeasurement> measurements) {
    Collections.sort(
        measurements,
        new Comparator<GnssMeasurement>() {
          @Override
          public int compare(GnssMeasurement o1, GnssMeasurement o2) {
            return Double.compare(o2.getCn0DbHz(), o1.getCn0DbHz());
          }
        });
    return measurements;
  }

  /**
   * An utility class provides and keeps record of all color assignments to the satellite in the
   * plots. Each satellite will receive a unique color assignment through out every graph.
   */
  private static class ColorMap {

    private ArrayMap<Integer, Integer> mColorMap = new ArrayMap<>();
    private int mColorsAssigned = 0;
    /**
     * Source of Kelly's contrasting colors:
     * https://medium.com/@rjurney/kellys-22-colours-of-maximum-contrast-58edb70c90d1
     */
    private static final String[] CONTRASTING_COLORS = {
      "#222222", "#F3C300", "#875692", "#F38400", "#A1CAF1", "#BE0032", "#C2B280", "#848482",
      "#008856", "#E68FAC", "#0067A5", "#F99379", "#604E97", "#F6A600", "#B3446C", "#DCD300",
      "#882D17", "#8DB600", "#654522", "#E25822", "#2B3D26"
    };

    private final Random mRandom = new Random();

    private int getColor(int svId, int constellationType) {
      // Assign the color from Kelly's 21 contrasting colors to satellites first, if all color
      // has been assigned, use a random color and record in {@link mColorMap}.
      if (mColorMap.containsKey(constellationType * 1000 + svId)) {
        return mColorMap.get(getUniqueSatelliteIdentifier(constellationType, svId));
      }
      if (this.mColorsAssigned < CONTRASTING_COLORS.length) {
        int color = Color.parseColor(CONTRASTING_COLORS[mColorsAssigned++]);
        mColorMap.put(getUniqueSatelliteIdentifier(constellationType, svId), color);
        return color;
      }
      int color = Color.argb(255, mRandom.nextInt(256), mRandom.nextInt(256), mRandom.nextInt(256));
      mColorMap.put(getUniqueSatelliteIdentifier(constellationType, svId), color);
      return color;
    }
  }

  private static int getUniqueSatelliteIdentifier(int constellationType, int svID) {
    return constellationType * 1000 + svID;
  }

  /**
   * An utility class stores and maintains all the data sets and corresponding renders. We use 0 as
   * the {@code dataSetIndex} of all constellations and 1 - 6 as the {@code dataSetIndex} of each
   * satellite constellations
   */
  private static class DataSetManager {
    /** The Y min and max of each plot */
    private static final int[][] RENDER_HEIGHTS = {{5, 45}, {-60, 60}};
    /**
     *
     *
     * <ul>
     *   <li>A list of constellation prefix
     *   <li>G : GPS, US Constellation
     *   <li>S : Satellite-based Augmentation System
     *   <li>R : GLONASS, Russia Constellation
     *   <li>J : QZSS, Japan Constellation
     *   <li>C : BEIDOU China Constellation
     *   <li>E : GALILEO EU Constellation
     * </ul>
     */
    private static final String[] CONSTELLATION_PREFIX = {"G", "S", "R", "J", "C", "E"};

    private final List<ArrayMap<Integer, Integer>>[] mSatelliteIndex;
    private final List<ArrayMap<Integer, Integer>>[] mSatelliteConstellationIndex;
    private final List<XYMultipleSeriesDataset>[] mDataSetList;
    private final List<XYMultipleSeriesRenderer>[] mRendererList;
    private final Context mContext;
    private final ColorMap mColorMap;

    public DataSetManager(
        int numberOfTabs, int numberOfConstellations, Context context, ColorMap colorMap) {
      mDataSetList = new ArrayList[numberOfTabs];
      mRendererList = new ArrayList[numberOfTabs];
      mSatelliteIndex = new ArrayList[numberOfTabs];
      mSatelliteConstellationIndex = new ArrayList[numberOfTabs];
      mContext = context;
      mColorMap = colorMap;

      // Preparing data sets and renderer for all six constellations
      for (int i = 0; i < numberOfTabs; i++) {
        mDataSetList[i] = new ArrayList<>();
        mRendererList[i] = new ArrayList<>();
        mSatelliteIndex[i] = new ArrayList<>();
        mSatelliteConstellationIndex[i] = new ArrayList<>();
        for (int k = 0; k <= numberOfConstellations; k++) {
          mSatelliteIndex[i].add(new ArrayMap<Integer, Integer>());
          mSatelliteConstellationIndex[i].add(new ArrayMap<Integer, Integer>());
          XYMultipleSeriesRenderer tempRenderer = new XYMultipleSeriesRenderer();
          setUpRenderer(tempRenderer, i);
          mRendererList[i].add(tempRenderer);
          XYMultipleSeriesDataset tempDataSet = new XYMultipleSeriesDataset();
          mDataSetList[i].add(tempDataSet);
        }
      }
    }

    // The constellation type should range from 1 to 6
    private String getConstellationPrefix(int constellationType) {
      if (constellationType <= GnssStatus.CONSTELLATION_UNKNOWN
          || constellationType > NUMBER_OF_CONSTELLATIONS) {
        return "";
      }
      return CONSTELLATION_PREFIX[constellationType - 1];
    }

    /** Returns the multiple series data set at specific tab and index */
    private XYMultipleSeriesDataset getDataSet(int tab, int dataSetIndex) {
      return mDataSetList[tab].get(dataSetIndex);
    }

    /** Returns the multiple series renderer set at specific tab and index */
    private XYMultipleSeriesRenderer getRenderer(int tab, int dataSetIndex) {
      return mRendererList[tab].get(dataSetIndex);
    }

    /**
     * Adds a value into the both the data set containing all constellations and individual data set
     * of the constellation of the satellite
     */
    private void addValue(
        int tab, int constellationType, int svID, double timeInSeconds, double value) {
      XYMultipleSeriesDataset dataSetAll = getDataSet(tab, DATA_SET_INDEX_ALL);
      XYMultipleSeriesRenderer rendererAll = getRenderer(tab, DATA_SET_INDEX_ALL);
      value = Double.parseDouble(sDataFormat.format(value));
      if (hasSeen(constellationType, svID, tab)) {
        // If the satellite has been seen before, we retrieve the dataseries it is add and add new
        // data
        dataSetAll
            .getSeriesAt(mSatelliteIndex[tab].get(constellationType).get(svID))
            .add(timeInSeconds, value);
        mDataSetList[tab]
            .get(constellationType)
            .getSeriesAt(mSatelliteConstellationIndex[tab].get(constellationType).get(svID))
            .add(timeInSeconds, value);
      } else {
        // If the satellite has not been seen before, we create new dataset and renderer before
        // adding data
        mSatelliteIndex[tab].get(constellationType).put(svID, dataSetAll.getSeriesCount());
        mSatelliteConstellationIndex[tab]
            .get(constellationType)
            .put(svID, mDataSetList[tab].get(constellationType).getSeriesCount());
        XYSeries tempSeries = new XYSeries(CONSTELLATION_PREFIX[constellationType - 1] + svID);
        tempSeries.add(timeInSeconds, value);
        dataSetAll.addSeries(tempSeries);
        mDataSetList[tab].get(constellationType).addSeries(tempSeries);
        XYSeriesRenderer tempRenderer = new XYSeriesRenderer();
        tempRenderer.setLineWidth(5);
        tempRenderer.setColor(mColorMap.getColor(svID, constellationType));
        rendererAll.addSeriesRenderer(tempRenderer);
        mRendererList[tab].get(constellationType).addSeriesRenderer(tempRenderer);
      }
    }

    /**
     * Creates a discontinuity of the satellites that has been seen but not reported in this batch
     * of measurements
     */
    private void fillInDiscontinuity(int tab, double referenceTimeSeconds) {
      for (XYMultipleSeriesDataset dataSet : mDataSetList[tab]) {
        for (int i = 0; i < dataSet.getSeriesCount(); i++) {
          if (dataSet.getSeriesAt(i).getMaxX() < referenceTimeSeconds) {
            dataSet.getSeriesAt(i).add(referenceTimeSeconds, MathHelper.NULL_VALUE);
          }
        }
      }
    }

    /** Returns a boolean indicating whether the input satellite has been seen. */
    private boolean hasSeen(int constellationType, int svID, int tab) {
      return mSatelliteIndex[tab].get(constellationType).containsKey(svID);
    }

    /** Set up a {@link XYMultipleSeriesRenderer} with the specs customized per plot tab. */
    private void setUpRenderer(XYMultipleSeriesRenderer renderer, int tabNumber) {
      renderer.setXAxisMin(0);
      renderer.setXAxisMax(60);
      renderer.setYAxisMin(RENDER_HEIGHTS[tabNumber][0]);
      renderer.setYAxisMax(RENDER_HEIGHTS[tabNumber][1]);
      renderer.setYAxisAlign(Align.RIGHT, 0);
      renderer.setLegendTextSize(30);
      renderer.setLabelsTextSize(30);
      renderer.setYLabelsColor(0, Color.BLACK);
      renderer.setXLabelsColor(Color.BLACK);
      renderer.setFitLegend(true);
      renderer.setShowGridX(true);
      renderer.setMargins(new int[] {10, 10, 30, 10});
      // setting the plot untouchable
      renderer.setZoomEnabled(false, false);
      renderer.setPanEnabled(false, true);
      renderer.setClickEnabled(false);
      renderer.setMarginsColor(Color.WHITE);
      renderer.setChartTitle(
          mContext.getResources().getStringArray(R.array.plot_titles)[tabNumber]);
      renderer.setChartTitleTextSize(50);
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/RealTimePositionVelocityCalculator.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.graphics.Color;
import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.Location;
import android.location.LocationManager;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.util.Log;
import com.google.android.apps.location.gps.gnsslogger.ResultFragment.UIResultComponent;
import com.google.location.lbs.gnss.gps.pseudorange.GpsMathOperations;
import com.google.location.lbs.gnss.gps.pseudorange.GpsNavigationMessageStore;
import com.google.location.lbs.gnss.gps.pseudorange.PseudorangePositionVelocityFromRealTimeEvents;
import java.text.DecimalFormat;
import java.util.concurrent.TimeUnit;

/**
 * A class that handles real time position and velocity calculation, passing {@link
 * GnssMeasurementsEvent} instances to the {@link PseudorangePositionVelocityFromRealTimeEvents}
 * whenever a new raw measurement is received in order to compute a new position solution. The
 * computed position and velocity solutions are passed to the {@link ResultFragment} to be
 * visualized.
 */
public class RealTimePositionVelocityCalculator implements MeasurementListener {
  /** Residual analysis where user disabled residual plots */
  public static final int RESIDUAL_MODE_DISABLED = -1;

  /** Residual analysis where the user is not moving */
  public static final int RESIDUAL_MODE_STILL = 0;

  /** Residual analysis where the user is moving */
  public static final int RESIDUAL_MODE_MOVING = 1;

  /** Residual analysis where the user chose to enter a LLA input as their position */
  public static final int RESIDUAL_MODE_AT_INPUT_LOCATION = 2;

  private static final long EARTH_RADIUS_METERS = 6371000;
  private PseudorangePositionVelocityFromRealTimeEvents
      mPseudorangePositionVelocityFromRealTimeEvents;
  private HandlerThread mPositionVelocityCalculationHandlerThread;
  private Handler mMyPositionVelocityCalculationHandler;
  private int mCurrentColor = Color.rgb(0x4a, 0x5f, 0x70);
  private int mCurrentColorIndex = 0;
  private boolean mAllowShowingRawResults = false;
  private MapFragment mMapFragment;
  private MainActivity mMainActivity;
  private PlotFragment mPlotFragment;
  private int[] mRgbColorArray = {
    Color.rgb(0x4a, 0x5f, 0x70),
    Color.rgb(0x7f, 0x82, 0x5f),
    Color.rgb(0xbf, 0x90, 0x76),
    Color.rgb(0x82, 0x4e, 0x4e),
    Color.rgb(0x66, 0x77, 0x7d)
  };
  private int mResidualPlotStatus;
  private double[] mGroundTruth = null;
  private int mPositionSolutionCount = 0;

  public RealTimePositionVelocityCalculator() {
    mPositionVelocityCalculationHandlerThread =
        new HandlerThread("Position From Realtime Pseudoranges");
    mPositionVelocityCalculationHandlerThread.start();
    mMyPositionVelocityCalculationHandler =
        new Handler(mPositionVelocityCalculationHandlerThread.getLooper());

    final Runnable r =
        new Runnable() {
          @Override
          public void run() {
            try {
              mPseudorangePositionVelocityFromRealTimeEvents =
                  new PseudorangePositionVelocityFromRealTimeEvents();
            } catch (Exception e) {
              Log.e(
                  MeasurementProvider.TAG,
                  " Exception in constructing PseudorangePositionFromRealTimeEvents : ",
                  e);
            }
          }
        };

    mMyPositionVelocityCalculationHandler.post(r);
  }

  private UIResultComponent uiResultComponent;

  public synchronized UIResultComponent getUiResultComponent() {
    return uiResultComponent;
  }

  public synchronized void setUiResultComponent(UIResultComponent value) {
    uiResultComponent = value;
  }

  @Override
  public void onProviderEnabled(String provider) {}

  @Override
  public void onProviderDisabled(String provider) {}

  @Override
  public void onGnssStatusChanged(GnssStatus gnssStatus) {}

  /**
   * Update the reference location in {@link PseudorangePositionVelocityFromRealTimeEvents} if the
   * received location is a network location. Otherwise, update the {@link ResultFragment} to
   * visualize both GPS location computed by the device and the one computed from the raw data.
   */
  @Override
  public void onLocationChanged(final Location location) {
    if (location.getProvider().equals(LocationManager.NETWORK_PROVIDER)) {
      final Runnable r =
          new Runnable() {
            @Override
            public void run() {
              if (mPseudorangePositionVelocityFromRealTimeEvents == null) {
                return;
              }
              try {
                mPseudorangePositionVelocityFromRealTimeEvents.setReferencePosition(
                    (int) (location.getLatitude() * 1E7),
                    (int) (location.getLongitude() * 1E7),
                    (int) (location.getAltitude() * 1E7));
              } catch (Exception e) {
                Log.e(MeasurementProvider.TAG, " Exception setting reference location : ", e);
              }
            }
          };

      mMyPositionVelocityCalculationHandler.post(r);

    } else if (location.getProvider().equals(LocationManager.GPS_PROVIDER)) {
      if (mAllowShowingRawResults) {
        final Runnable r =
            new Runnable() {
              @Override
              public void run() {
                if (mPseudorangePositionVelocityFromRealTimeEvents == null) {
                  return;
                }
                double[] posSolution =
                    mPseudorangePositionVelocityFromRealTimeEvents.getPositionSolutionLatLngDeg();
                double[] velSolution =
                    mPseudorangePositionVelocityFromRealTimeEvents.getVelocitySolutionEnuMps();
                double[] pvUncertainty =
                    mPseudorangePositionVelocityFromRealTimeEvents
                        .getPositionVelocityUncertaintyEnu();
                if (Double.isNaN(posSolution[0])) {
                  logPositionFromRawDataEvent("No Position Calculated Yet");
                  logPositionError("And no offset calculated yet...");
                } else {
                  if (mResidualPlotStatus != RESIDUAL_MODE_DISABLED
                      && mResidualPlotStatus != RESIDUAL_MODE_AT_INPUT_LOCATION) {
                    updateGroundTruth(posSolution);
                  }
                  String formattedLatDegree = new DecimalFormat("##.######").format(posSolution[0]);
                  String formattedLngDegree = new DecimalFormat("##.######").format(posSolution[1]);
                  String formattedAltMeters = new DecimalFormat("##.#").format(posSolution[2]);
                  logPositionFromRawDataEvent(
                      "latDegrees = "
                          + formattedLatDegree
                          + " lngDegrees = "
                          + formattedLngDegree
                          + "altMeters = "
                          + formattedAltMeters);
                  String formattedVelocityEastMps =
                      new DecimalFormat("##.###").format(velSolution[0]);
                  String formattedVelocityNorthMps =
                      new DecimalFormat("##.###").format(velSolution[1]);
                  String formattedVelocityUpMps =
                      new DecimalFormat("##.###").format(velSolution[2]);
                  logVelocityFromRawDataEvent(
                      "Velocity East = "
                          + formattedVelocityEastMps
                          + "mps"
                          + " Velocity North = "
                          + formattedVelocityNorthMps
                          + "mps"
                          + "Velocity Up = "
                          + formattedVelocityUpMps
                          + "mps");

                  String formattedPosUncertaintyEastMeters =
                      new DecimalFormat("##.###").format(pvUncertainty[0]);
                  String formattedPosUncertaintyNorthMeters =
                      new DecimalFormat("##.###").format(pvUncertainty[1]);
                  String formattedPosUncertaintyUpMeters =
                      new DecimalFormat("##.###").format(pvUncertainty[2]);
                  logPositionUncertainty(
                      "East = "
                          + formattedPosUncertaintyEastMeters
                          + "m North = "
                          + formattedPosUncertaintyNorthMeters
                          + "m Up = "
                          + formattedPosUncertaintyUpMeters
                          + "m");
                  String formattedVelUncertaintyEastMeters =
                      new DecimalFormat("##.###").format(pvUncertainty[3]);
                  String formattedVelUncertaintyNorthMeters =
                      new DecimalFormat("##.###").format(pvUncertainty[4]);
                  String formattedVelUncertaintyUpMeters =
                      new DecimalFormat("##.###").format(pvUncertainty[5]);
                  logVelocityUncertainty(
                      "East = "
                          + formattedVelUncertaintyEastMeters
                          + "mps North = "
                          + formattedVelUncertaintyNorthMeters
                          + "mps Up = "
                          + formattedVelUncertaintyUpMeters
                          + "mps");
                  String formattedOffsetMeters =
                      new DecimalFormat("##.######")
                          .format(
                              getDistanceMeters(
                                  location.getLatitude(),
                                  location.getLongitude(),
                                  posSolution[0],
                                  posSolution[1]));
                  logPositionError("position offset = " + formattedOffsetMeters + " meters");
                  String formattedSpeedOffsetMps =
                      new DecimalFormat("##.###")
                          .format(
                              Math.abs(
                                  location.getSpeed()
                                      - Math.sqrt(
                                          Math.pow(velSolution[0], 2)
                                              + Math.pow(velSolution[1], 2))));
                  logVelocityError("speed offset = " + formattedSpeedOffsetMps + " mps");
                }
                logLocationEvent("onLocationChanged: " + location);
                if (!Double.isNaN(posSolution[0])) {
                  updateMapViewWithPositions(
                      posSolution[0],
                      posSolution[1],
                      location.getLatitude(),
                      location.getLongitude(),
                      location.getTime());
                } else {
                  clearMapMarkers();
                }
              }
            };
        mMyPositionVelocityCalculationHandler.post(r);
      }
    }
  }

  private void clearMapMarkers() {
    mMapFragment.clearMarkers();
  }

  private void updateMapViewWithPositions(
      double latDegRaw,
      double lngDegRaw,
      double latDegDevice,
      double lngDegDevice,
      long timeMillis) {
    mMapFragment.updateMapViewWithPositions(
        latDegRaw, lngDegRaw, latDegDevice, lngDegDevice, timeMillis);
  }

  @Override
  public void onLocationStatusChanged(String provider, int status, Bundle extras) {}

  @Override
  public void onGnssMeasurementsReceived(final GnssMeasurementsEvent event) {
    mAllowShowingRawResults = true;
    final Runnable r =
        new Runnable() {
          @Override
          public void run() {
            mMainActivity.runOnUiThread(
                new Runnable() {
                  @Override
                  public void run() {
                    mPlotFragment.updateCnoTab(event);
                  }
                });
            if (mPseudorangePositionVelocityFromRealTimeEvents == null) {
              return;
            }
            try {
              if (mResidualPlotStatus != RESIDUAL_MODE_DISABLED
                  && mResidualPlotStatus != RESIDUAL_MODE_AT_INPUT_LOCATION) {
                // The position at last epoch is used for the residual analysis.
                // This is happening by updating the ground truth for pseudorange before using the
                // new arriving pseudoranges to compute a new position.
                mPseudorangePositionVelocityFromRealTimeEvents
                    .setCorrectedResidualComputationTruthLocationLla(mGroundTruth);
              }
              mPseudorangePositionVelocityFromRealTimeEvents
                  .computePositionVelocitySolutionsFromRawMeas(event);
              // Running on main thread instead of in parallel will improve the thread safety
              if (mResidualPlotStatus != RESIDUAL_MODE_DISABLED) {
                mMainActivity.runOnUiThread(
                    new Runnable() {
                      @Override
                      public void run() {
                        mPlotFragment.updatePseudorangeResidualTab(
                            mPseudorangePositionVelocityFromRealTimeEvents
                                .getPseudorangeResidualsMeters(),
                            TimeUnit.NANOSECONDS.toSeconds(event.getClock().getTimeNanos()));
                      }
                    });
              } else {
                mMainActivity.runOnUiThread(
                    new Runnable() {
                      @Override
                      public void run() {
                        // Here we create gaps when the residual plot is disabled
                        mPlotFragment.updatePseudorangeResidualTab(
                            GpsMathOperations.createAndFillArray(
                                GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES, Double.NaN),
                            TimeUnit.NANOSECONDS.toSeconds(event.getClock().getTimeNanos()));
                      }
                    });
              }
            } catch (Exception e) {
              e.printStackTrace();
            }
          }
        };
    mMyPositionVelocityCalculationHandler.post(r);
  }

  @Override
  public void onGnssMeasurementsStatusChanged(int status) {}

  @Override
  public void onGnssNavigationMessageReceived(GnssNavigationMessage event) {
    if (event.getType() == GnssNavigationMessage.TYPE_GPS_L1CA) {
      mPseudorangePositionVelocityFromRealTimeEvents.parseHwNavigationMessageUpdates(event);
    }
  }

  @Override
  public void onGnssNavigationMessageStatusChanged(int status) {}

  @Override
  public void onNmeaReceived(long l, String s) {}

  @Override
  public void onListenerRegistration(String listener, boolean result) {}

  private void logEvent(String tag, String message, int color) {
    String composedTag = MeasurementProvider.TAG + tag;
    Log.d(composedTag, message);
    logText(tag, message, color);
  }

  private void logText(String tag, String text, int color) {
    UIResultComponent component = getUiResultComponent();
    if (component != null) {
      component.logTextResults(tag, text, color);
    }
  }

  public void logLocationEvent(String event) {
    mCurrentColor = getNextColor();
    logEvent("Location", event, mCurrentColor);
  }

  private void logPositionFromRawDataEvent(String event) {
    logEvent("Calculated Position From Raw Data", event + "\n", mCurrentColor);
  }

  private void logVelocityFromRawDataEvent(String event) {
    logEvent("Calculated Velocity From Raw Data", event + "\n", mCurrentColor);
  }

  private void logPositionError(String event) {
    logEvent(
        "Offset between the reported position and Google's WLS position based on reported "
            + "measurements",
        event + "\n",
        mCurrentColor);
  }

  private void logVelocityError(String event) {
    logEvent(
        "Offset between the reported velocity and "
            + "Google's computed velocity based on reported measurements ",
        event + "\n",
        mCurrentColor);
  }

  private void logPositionUncertainty(String event) {
    logEvent("Uncertainty of the calculated position from Raw Data", event + "\n", mCurrentColor);
  }

  private void logVelocityUncertainty(String event) {
    logEvent("Uncertainty of the calculated velocity from Raw Data", event + "\n", mCurrentColor);
  }

  private synchronized int getNextColor() {
    ++mCurrentColorIndex;
    return mRgbColorArray[mCurrentColorIndex % mRgbColorArray.length];
  }

  /** Return the distance (measured along the surface of the sphere) between 2 points */
  public double getDistanceMeters(
      double lat1Degree, double lng1Degree, double lat2Degree, double lng2Degree) {

    double deltaLatRadian = Math.toRadians(lat2Degree - lat1Degree);
    double deltaLngRadian = Math.toRadians(lng2Degree - lng1Degree);

    double a =
        Math.sin(deltaLatRadian / 2) * Math.sin(deltaLatRadian / 2)
            + Math.cos(Math.toRadians(lat1Degree))
                * Math.cos(Math.toRadians(lat2Degree))
                * Math.sin(deltaLngRadian / 2)
                * Math.sin(deltaLngRadian / 2);
    double angularDistanceRad = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return EARTH_RADIUS_METERS * angularDistanceRad;
  }

  /** Update the ground truth for pseudorange residual analysis based on the user activity. */
  private synchronized void updateGroundTruth(double[] posSolution) {

    // In case of switching between modes, last ground truth from previous mode will be used.
    if (mGroundTruth == null) {
      // If mGroundTruth has not been initialized, we set it to be the same as position solution
      mGroundTruth = new double[] {0.0, 0.0, 0.0};
      mGroundTruth[0] = posSolution[0];
      mGroundTruth[1] = posSolution[1];
      mGroundTruth[2] = posSolution[2];
    } else if (mResidualPlotStatus == RESIDUAL_MODE_STILL) {
      // If the user is standing still, we average our WLS position solution
      // Reference: https://en.wikipedia.org/wiki/Moving_average#Cumulative_moving_average
      mGroundTruth[0] =
          (mGroundTruth[0] * mPositionSolutionCount + posSolution[0])
              / (mPositionSolutionCount + 1);
      mGroundTruth[1] =
          (mGroundTruth[1] * mPositionSolutionCount + posSolution[1])
              / (mPositionSolutionCount + 1);
      mGroundTruth[2] =
          (mGroundTruth[2] * mPositionSolutionCount + posSolution[2])
              / (mPositionSolutionCount + 1);
      mPositionSolutionCount++;
    } else if (mResidualPlotStatus == RESIDUAL_MODE_MOVING) {
      // If the user is moving fast, we use single WLS position solution
      mGroundTruth[0] = posSolution[0];
      mGroundTruth[1] = posSolution[1];
      mGroundTruth[2] = posSolution[2];
      mPositionSolutionCount = 0;
    }
  }

  /** Sets {@link MapFragment} for receiving WLS location update */
  public void setMapFragment(MapFragment mapFragment) {
    this.mMapFragment = mapFragment;
  }

  /**
   * Sets {@link PlotFragment} for receiving Gnss measurement and residual computation results for
   * plot
   */
  public void setPlotFragment(PlotFragment plotFragment) {
    this.mPlotFragment = plotFragment;
  }

  /** Sets {@link MainActivity} for running some UI tasks on UI thread */
  public void setMainActivity(MainActivity mainActivity) {
    this.mMainActivity = mainActivity;
  }

  /**
   * Sets the ground truth mode in {@link PseudorangePositionVelocityFromRealTimeEvents} for
   * calculating corrected pseudorange residuals, also logs the change in ResultFragment
   */
  public void setResidualPlotMode(int residualPlotStatus, double[] fixedGroundTruth) {
    mResidualPlotStatus = residualPlotStatus;
    if (mPseudorangePositionVelocityFromRealTimeEvents == null) {
      return;
    }
    switch (mResidualPlotStatus) {
      case RESIDUAL_MODE_MOVING:
        mPseudorangePositionVelocityFromRealTimeEvents
            .setCorrectedResidualComputationTruthLocationLla(mGroundTruth);
        logEvent("Residual Plot", "Mode is set to moving", mCurrentColor);
        break;

      case RESIDUAL_MODE_STILL:
        mPseudorangePositionVelocityFromRealTimeEvents
            .setCorrectedResidualComputationTruthLocationLla(mGroundTruth);
        logEvent("Residual Plot", "Mode is set to still", mCurrentColor);
        break;

      case RESIDUAL_MODE_AT_INPUT_LOCATION:
        mPseudorangePositionVelocityFromRealTimeEvents
            .setCorrectedResidualComputationTruthLocationLla(fixedGroundTruth);
        logEvent("Residual Plot", "Mode is set to fixed ground truth", mCurrentColor);
        break;

      case RESIDUAL_MODE_DISABLED:
        mGroundTruth = null;
        mPseudorangePositionVelocityFromRealTimeEvents
            .setCorrectedResidualComputationTruthLocationLla(mGroundTruth);
        logEvent("Residual Plot", "Mode is set to Disabled", mCurrentColor);
        break;

      default:
        mPseudorangePositionVelocityFromRealTimeEvents
            .setCorrectedResidualComputationTruthLocationLla(null);
    }
  }

  @Override
  public void onTTFFReceived(long l) {}
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/ResultFragment.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.text.Editable;
import android.text.SpannableStringBuilder;
import android.text.style.ForegroundColorSpan;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ScrollView;
import android.widget.TextView;
import androidx.fragment.app.Fragment;

/** The UI fragment that hosts a logging view. */
public class ResultFragment extends Fragment {

  private TextView mLogView;
  private ScrollView mScrollView;

  private RealTimePositionVelocityCalculator mPositionVelocityCalculator;

  private final UIResultComponent mUiComponent = new UIResultComponent();

  public void setPositionVelocityCalculator(RealTimePositionVelocityCalculator value) {
    mPositionVelocityCalculator = value;
  }

  @Override
  public View onCreateView(
      LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    View newView = inflater.inflate(R.layout.results_log, container, false /* attachToRoot */);
    mLogView = (TextView) newView.findViewById(R.id.log_view);
    mScrollView = (ScrollView) newView.findViewById(R.id.log_scroll);

    RealTimePositionVelocityCalculator currentPositionVelocityCalculator =
        mPositionVelocityCalculator;
    if (currentPositionVelocityCalculator != null) {
      currentPositionVelocityCalculator.setUiResultComponent(mUiComponent);
    }

    Button start = (Button) newView.findViewById(R.id.start_log);
    start.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            mScrollView.fullScroll(View.FOCUS_UP);
          }
        });

    Button end = (Button) newView.findViewById(R.id.end_log);
    end.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            mScrollView.fullScroll(View.FOCUS_DOWN);
          }
        });

    Button clear = (Button) newView.findViewById(R.id.clear_log);
    clear.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            mLogView.setText("");
          }
        });
    return newView;
  }

  /**
   * A facade for UI and Activity related operations that are required for {@link
   * MeasurementListener}s.
   */
  public class UIResultComponent {

    private static final int MAX_LENGTH = 12000;
    private static final int LOWER_THRESHOLD = (int) (MAX_LENGTH * 0.5);

    public synchronized void logTextResults(final String tag, final String text, int color) {
      final SpannableStringBuilder builder = new SpannableStringBuilder();
      builder.append(tag).append(" | ").append(text).append("\n");

      builder.setSpan(
          new ForegroundColorSpan(color),
          0 /* start */,
          builder.length(),
          SpannableStringBuilder.SPAN_INCLUSIVE_EXCLUSIVE);

      Activity activity = getActivity();
      if (activity == null) {
        return;
      }
      activity.runOnUiThread(
          new Runnable() {
            @Override
            public void run() {
              mLogView.append(builder);
              SharedPreferences sharedPreferences =
                  PreferenceManager.getDefaultSharedPreferences(getActivity());
              Editable editable = mLogView.getEditableText();
              int length = editable.length();
              if (length > MAX_LENGTH) {
                editable.delete(0, length - LOWER_THRESHOLD);
              }
              if (sharedPreferences.getBoolean(
                  SettingsFragment.PREFERENCE_KEY_AUTO_SCROLL, false /*default return value*/)) {
                mScrollView.post(
                    new Runnable() {
                      @Override
                      public void run() {
                        mScrollView.fullScroll(View.FOCUS_DOWN);
                      }
                    });
              }
            }
          });
    }

    public void startActivity(Intent intent) {
      getActivity().startActivity(intent);
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/SettingsFragment.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.view.ViewGroup.LayoutParams;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.CompoundButton.OnCheckedChangeListener;
import android.widget.PopupWindow;
import android.widget.PopupWindow.OnDismissListener;
import android.widget.Spinner;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;
import androidx.fragment.app.Fragment;
import java.lang.reflect.InvocationTargetException;

/** The UI fragment showing a set of configurable settings for the client to request GPS data. */
public class SettingsFragment extends Fragment {

  public static final String TAG = ":SettingsFragment";

  /** Position in the drop down menu of the auto ground truth mode */
  private static int AUTO_GROUND_TRUTH_MODE = 3;

  /** Key in the {@link SharedPreferences} indicating whether auto-scroll has been enabled */
  protected static String PREFERENCE_KEY_AUTO_SCROLL = "autoScroll";

  private MeasurementProvider mGpsContainer;
  private HelpDialog helpDialog;

  /**
   * The {@link RealTimePositionVelocityCalculator} set for receiving the ground truth mode switch
   */
  private RealTimePositionVelocityCalculator mRealTimePositionVelocityCalculator;

  /** User selection of ground truth mode, initially set to be disabled */
  private int mResidualSetting = RealTimePositionVelocityCalculator.RESIDUAL_MODE_DISABLED;

  /** The reference ground truth location by user input. */
  private double[] mFixedReferenceLocation = null;

  /** {@link GroundTruthModeSwitcher} to receive update from AR result broadcast */
  private GroundTruthModeSwitcher mModeSwitcher;

  public void setGpsContainer(MeasurementProvider value) {
    mGpsContainer = value;
  }

  /** Set up {@link MainActivity} to receive update from AR result broadcast */
  public void setAutoModeSwitcher(GroundTruthModeSwitcher modeSwitcher) {
    mModeSwitcher = modeSwitcher;
  }

  /**
   * Set up {@code RealTimePositionVelocityCalculator} for receiving changes in ground truth mode
   */
  public void setRealTimePositionVelocityCalculator(
      RealTimePositionVelocityCalculator realTimePositionVelocityCalculator) {
    mRealTimePositionVelocityCalculator = realTimePositionVelocityCalculator;
  }

  @Override
  public View onCreateView(
      LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    final View view = inflater.inflate(R.layout.fragment_main, container, false /* attachToRoot */);

    final Switch registerLocation = (Switch) view.findViewById(R.id.register_location);
    final TextView registerLocationLabel =
        (TextView) view.findViewById(R.id.register_location_label);
    // set the switch to OFF
    registerLocation.setChecked(false);
    registerLocationLabel.setText("Switch is OFF");
    registerLocation.setOnCheckedChangeListener(
        new OnCheckedChangeListener() {

          @Override
          public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

            if (isChecked) {
              mGpsContainer.registerLocation();
              mGpsContainer.registerFusedLocation();
              registerLocationLabel.setText("Switch is ON");
            } else {
              mGpsContainer.unregisterLocation();
              mGpsContainer.unRegisterFusedLocation();
              registerLocationLabel.setText("Switch is OFF");
            }
          }
        });

    final Switch registerMeasurements = (Switch) view.findViewById(R.id.register_measurements);
    final TextView registerMeasurementsLabel =
        (TextView) view.findViewById(R.id.register_measurement_label);
    // set the switch to OFF
    registerMeasurements.setChecked(false);
    registerMeasurementsLabel.setText("Switch is OFF");
    registerMeasurements.setOnCheckedChangeListener(
        new OnCheckedChangeListener() {

          @Override
          public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

            if (isChecked) {
              mGpsContainer.registerMeasurements();
              registerMeasurementsLabel.setText("Switch is ON");
            } else {
              mGpsContainer.unregisterMeasurements();
              registerMeasurementsLabel.setText("Switch is OFF");
            }
          }
        });

    final Switch registerNavigation = (Switch) view.findViewById(R.id.register_navigation);
    final TextView registerNavigationLabel =
        (TextView) view.findViewById(R.id.register_navigation_label);
    // set the switch to OFF
    registerNavigation.setChecked(false);
    registerNavigationLabel.setText("Switch is OFF");
    registerNavigation.setOnCheckedChangeListener(
        new OnCheckedChangeListener() {

          @Override
          public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

            if (isChecked) {
              mGpsContainer.registerNavigation();
              registerNavigationLabel.setText("Switch is ON");
            } else {
              mGpsContainer.unregisterNavigation();
              registerNavigationLabel.setText("Switch is OFF");
            }
          }
        });

    final Switch registerGpsStatus = (Switch) view.findViewById(R.id.register_status);
    final TextView registerGpsStatusLabel =
        (TextView) view.findViewById(R.id.register_status_label);
    // set the switch to OFF
    registerGpsStatus.setChecked(false);
    registerGpsStatusLabel.setText("Switch is OFF");
    registerGpsStatus.setOnCheckedChangeListener(
        new OnCheckedChangeListener() {

          @Override
          public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

            if (isChecked) {
              mGpsContainer.registerGnssStatus();
              registerGpsStatusLabel.setText("Switch is ON");
            } else {
              mGpsContainer.unregisterGpsStatus();
              registerGpsStatusLabel.setText("Switch is OFF");
            }
          }
        });

    final Switch registerNmea = (Switch) view.findViewById(R.id.register_nmea);
    final TextView registerNmeaLabel = (TextView) view.findViewById(R.id.register_nmea_label);
    // set the switch to OFF
    registerNmea.setChecked(false);
    registerNmeaLabel.setText("Switch is OFF");
    registerNmea.setOnCheckedChangeListener(
        new OnCheckedChangeListener() {

          @Override
          public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

            if (isChecked) {
              mGpsContainer.registerNmea();
              registerNmeaLabel.setText("Switch is ON");
            } else {
              mGpsContainer.unregisterNmea();
              registerNmeaLabel.setText("Switch is OFF");
            }
          }
        });
    final Switch autoScroll = (Switch) view.findViewById(R.id.auto_scroll_on);
    final TextView turnOnAutoScroll = (TextView) view.findViewById(R.id.turn_on_auto_scroll);
    turnOnAutoScroll.setText("Switch is OFF");
    autoScroll.setOnCheckedChangeListener(
        new OnCheckedChangeListener() {
          @Override
          public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
            SharedPreferences sharedPreferences =
                PreferenceManager.getDefaultSharedPreferences(getActivity());
            Editor editor = sharedPreferences.edit();
            if (isChecked) {
              editor.putBoolean(PREFERENCE_KEY_AUTO_SCROLL, true);
              editor.apply();
              turnOnAutoScroll.setText("Switch is ON");
            } else {
              editor.putBoolean(PREFERENCE_KEY_AUTO_SCROLL, false);
              editor.apply();
              turnOnAutoScroll.setText("Switch is OFF");
            }
          }
        });

    final Switch residualPlotSwitch = (Switch) view.findViewById(R.id.residual_plot_enabled);
    final TextView turnOnResidual = (TextView) view.findViewById(R.id.turn_on_residual_plot);
    turnOnResidual.setText("Switch is OFF");
    residualPlotSwitch.setOnCheckedChangeListener(
        new OnCheckedChangeListener() {
          @Override
          public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
            if (isChecked) {

              LayoutInflater inflater =
                  (LayoutInflater) getActivity().getSystemService(Context.LAYOUT_INFLATER_SERVICE);
              View layout =
                  inflater.inflate(
                      R.layout.pop_up_window, (ViewGroup) getActivity().findViewById(R.id.pop));

              // Find UI elements in pop up window
              final Spinner residualSpinner = layout.findViewById(R.id.residual_spinner);
              Button buttonOk = layout.findViewById(R.id.popup_button_ok);
              Button buttonCancel = layout.findViewById(R.id.popup_button_cancel);
              final TextView longitudeInput = layout.findViewById(R.id.longitude_input);
              final TextView latitudeInput = layout.findViewById(R.id.latitude_input);
              final TextView altitudeInput = layout.findViewById(R.id.altitude_input);

              // Set up pop up window attributes
              final PopupWindow popupWindow =
                  new PopupWindow(layout, LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
              popupWindow.setOutsideTouchable(false);
              popupWindow.showAtLocation(
                  view.findViewById(R.id.setting_root), Gravity.CENTER, 0, 0);
              View container = (View) popupWindow.getContentView().getParent();
              WindowManager wm =
                  (WindowManager) getActivity().getSystemService(Context.WINDOW_SERVICE);
              WindowManager.LayoutParams params =
                  (WindowManager.LayoutParams) container.getLayoutParams();
              params.flags = WindowManager.LayoutParams.FLAG_DIM_BEHIND;
              params.dimAmount = 0.5f;
              wm.updateViewLayout(container, params);
              mResidualSetting = RealTimePositionVelocityCalculator.RESIDUAL_MODE_DISABLED;
              // When the window is dismissed same as cancel
              popupWindow.setOnDismissListener(
                  new OnDismissListener() {
                    @Override
                    public void onDismiss() {
                      if (mResidualSetting
                          == RealTimePositionVelocityCalculator.RESIDUAL_MODE_DISABLED) {
                        residualPlotSwitch.setChecked(false);
                      } else {
                        mRealTimePositionVelocityCalculator.setResidualPlotMode(
                            mResidualSetting, mFixedReferenceLocation);
                        turnOnResidual.setText("Switch is ON");
                      }
                    }
                  });

              buttonCancel.setOnClickListener(
                  new OnClickListener() {
                    @Override
                    public void onClick(View v) {
                      popupWindow.dismiss();
                    }
                  });

              // Button handler to dismiss the window and store settings
              buttonOk.setOnClickListener(
                  new OnClickListener() {
                    @Override
                    public void onClick(View v) {
                      double longitudeDegrees =
                          longitudeInput.getText().toString().equals("")
                              ? Double.NaN
                              : Double.parseDouble(longitudeInput.getText().toString());
                      double latitudeDegrees =
                          latitudeInput.getText().toString().equals("")
                              ? Double.NaN
                              : Double.parseDouble(latitudeInput.getText().toString());
                      double altitudeMeters =
                          altitudeInput.getText().toString().equals("")
                              ? Double.NaN
                              : Double.parseDouble(altitudeInput.getText().toString());
                      mFixedReferenceLocation =
                          new double[] {latitudeDegrees, longitudeDegrees, altitudeMeters};
                      mResidualSetting = residualSpinner.getSelectedItemPosition();

                      // If user select auto, we need to put moving first and turn on AR updates
                      if (mResidualSetting == AUTO_GROUND_TRUTH_MODE) {
                        mResidualSetting = RealTimePositionVelocityCalculator.RESIDUAL_MODE_MOVING;
                        mModeSwitcher.setAutoSwitchGroundTruthModeEnabled(true);
                      }
                      popupWindow.dismiss();
                    }
                  });

            } else {
              mModeSwitcher.setAutoSwitchGroundTruthModeEnabled(false);
              mRealTimePositionVelocityCalculator.setResidualPlotMode(
                  RealTimePositionVelocityCalculator.RESIDUAL_MODE_DISABLED,
                  mFixedReferenceLocation);
              turnOnResidual.setText("Switch is OFF");
            }
          }
        });
    Button help = (Button) view.findViewById(R.id.help);
    helpDialog = new HelpDialog(getContext());
    helpDialog.setTitle("Help contents");
    helpDialog.create();

    help.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            helpDialog.show();
          }
        });

    Button exit = (Button) view.findViewById(R.id.exit);
    exit.setOnClickListener(
        new OnClickListener() {
          @Override
          public void onClick(View view) {
            getActivity().finishAffinity();
          }
        });

    TextView swInfo = (TextView) view.findViewById(R.id.sw_info);

    java.lang.reflect.Method method;
    LocationManager locationManager = mGpsContainer.getLocationManager();
    try {
      method = locationManager.getClass().getMethod("getGnssYearOfHardware");
      int hwYear = (int) method.invoke(locationManager);
      if (hwYear == 0) {
        swInfo.append("HW Year: " + "2015 or older \n");
      } else {
        swInfo.append("HW Year: " + hwYear + "\n");
      }

    } catch (NoSuchMethodException e) {
      logException("No such method exception: ", e);
      return null;
    } catch (IllegalAccessException e) {
      logException("Illegal Access exception: ", e);
      return null;
    } catch (InvocationTargetException e) {
      logException("Invocation Target Exception: ", e);
      return null;
    }

    String platformVersionString = Build.VERSION.RELEASE;
    swInfo.append("Platform: " + platformVersionString + "\n");
    int apiLevelInt = Build.VERSION.SDK_INT;
    swInfo.append("Api Level: " + apiLevelInt);

    return view;
  }

  private void logException(String errorMessage, Exception e) {
    Log.e(MeasurementProvider.TAG + TAG, errorMessage, e);
    Toast.makeText(getContext(), errorMessage, Toast.LENGTH_LONG).show();
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/TimerFragment.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import static com.google.common.base.Preconditions.checkState;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.Dialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.NumberPicker;
import androidx.fragment.app.DialogFragment;
import com.google.android.apps.location.gps.gnsslogger.TimerService.TimerListener;

/** A {@link Dialog} allowing "Hours", "Minutes", and "Seconds" to be selected for a timer */
public class TimerFragment extends DialogFragment {
  private TimerListener mListener;

  @Override
  public void onAttach(Activity activity) {
    super.onAttach(activity);

    checkState(
        getTargetFragment() instanceof TimerListener,
        "Target fragment is not instance of TimerListener");

    mListener = (TimerListener) getTargetFragment();
  }

  @Override
  public Dialog onCreateDialog(Bundle savedInstanceState) {
    AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());

    View view = getActivity().getLayoutInflater().inflate(R.layout.timer, null);
    final NumberPicker timerHours = (NumberPicker) view.findViewById(R.id.hours_picker);
    final NumberPicker timerMinutes = (NumberPicker) view.findViewById(R.id.minutes_picker);
    final NumberPicker timerSeconds = (NumberPicker) view.findViewById(R.id.seconds_picker);

    final TimerValues values;

    if (getArguments() != null) {
      values = TimerValues.fromBundle(getArguments());
    } else {
      values = new TimerValues(0 /* hours */, 0 /* minutes */, 0 /* seconds */);
    }

    values.configureHours(timerHours);
    values.configureMinutes(timerMinutes);
    values.configureSeconds(timerSeconds);

    builder.setTitle(R.string.timer_title);
    builder.setView(view);
    builder.setPositiveButton(
        R.string.timer_set,
        new DialogInterface.OnClickListener() {
          @Override
          public void onClick(DialogInterface dialog, int id) {
            mListener.processTimerValues(
                new TimerValues(
                    timerHours.getValue(), timerMinutes.getValue(), timerSeconds.getValue()));
          }
        });
    builder.setNeutralButton(
        R.string.timer_cancel,
        new DialogInterface.OnClickListener() {
          @Override
          public void onClick(DialogInterface dialog, int id) {
            mListener.processTimerValues(values);
          }
        });
    builder.setNegativeButton(
        R.string.timer_reset,
        new DialogInterface.OnClickListener() {
          @Override
          public void onClick(DialogInterface dialog, int id) {
            mListener.processTimerValues(
                new TimerValues(0 /* hours */, 0 /* minutes */, 0 /* seconds */));
          }
        });

    return builder.create();
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/TimerService.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.CountDownTimer;
import android.os.IBinder;
import androidx.core.app.NotificationChannelCompat;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;
import java.util.concurrent.TimeUnit;

/** A {@link Service} to be bound to that exposes a timer. */
public class TimerService extends Service {
  static final String TIMER_ACTION =
      String.format("%s.TIMER_UPDATE", TimerService.class.getPackage().getName());
  static final String EXTRA_KEY_TYPE = "type";
  static final String EXTRA_KEY_UPDATE_REMAINING = "remaining";
  static final byte TYPE_UNKNOWN = -1;
  static final byte TYPE_UPDATE = 0;
  static final byte TYPE_FINISH = 1;
  static final int NOTIFICATION_ID = 7777;

  private static final String NOTIFICATION_CHANNEL_ID = "gnss-logger-notification-channel";
  private final IBinder mBinder = new TimerBinder();
  private CountDownTimer mCountDownTimer;
  private boolean mTimerStarted;

  /** Handles response from {@link TimerFragment} */
  public interface TimerListener {
    /**
     * Process a {@link TimerValues} result
     *
     * @param values The set {@link TimerValues}
     */
    public void processTimerValues(TimerValues values);
  }

  /** A {@link Binder} that exposes a {@link TimerService}. */
  public class TimerBinder extends Binder {
    TimerService getService() {
      return TimerService.this;
    }
  }

  @Override
  public void onCreate() {
    mTimerStarted = false;
  }

  @Override
  public IBinder onBind(Intent intent) {
    NotificationChannelCompat channel =
        new NotificationChannelCompat.Builder(
                NOTIFICATION_CHANNEL_ID, NotificationManager.IMPORTANCE_DEFAULT)
            .setName(getResources().getString(R.string.timer_service_notification_channel_name))
            .setDescription(
                getResources().getString(R.string.timer_service_notification_channel_description))
            .build();
    NotificationManagerCompat manager = NotificationManagerCompat.from(this);
    manager.createNotificationChannel(channel);
    Notification notification =
        new NotificationCompat.Builder(this, NOTIFICATION_CHANNEL_ID).build();
    startForeground(NOTIFICATION_ID, notification);
    return mBinder;
  }

  @Override
  public void onDestroy() {
    if (mCountDownTimer != null) {
      mCountDownTimer.cancel();
    }
    mTimerStarted = false;
  }

  void setTimer(TimerValues values) {
    // Only allow setting when not already running
    if (!mTimerStarted) {
      mCountDownTimer =
          new CountDownTimer(
              values.getTotalMilliseconds(),
              TimeUnit.MILLISECONDS.convert(1, TimeUnit.SECONDS) /* countDownInterval */) {
            @Override
            public void onTick(long millisUntilFinished) {
              Intent broadcast = new Intent(TIMER_ACTION);
              broadcast.putExtra(EXTRA_KEY_TYPE, TYPE_UPDATE);
              broadcast.putExtra(EXTRA_KEY_UPDATE_REMAINING, millisUntilFinished);
              LocalBroadcastManager.getInstance(TimerService.this).sendBroadcast(broadcast);
            }

            @Override
            public void onFinish() {
              mTimerStarted = false;
              Intent broadcast = new Intent(TIMER_ACTION);
              broadcast.putExtra(EXTRA_KEY_TYPE, TYPE_FINISH);
              LocalBroadcastManager.getInstance(TimerService.this).sendBroadcast(broadcast);
            }
          };
    }
  }

  void startTimer() {
    if ((mCountDownTimer != null) && !mTimerStarted) {
      mCountDownTimer.start();
      mTimerStarted = true;
    }
  }

  void stopTimer() {
    if (mCountDownTimer != null) {
      mCountDownTimer.cancel();
      mTimerStarted = false;
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/TimerValues.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import static com.google.common.base.Preconditions.checkArgument;

import android.os.Bundle;
import android.widget.NumberPicker;
import java.util.concurrent.TimeUnit;

/** A representation of a time as "hours:minutes:seconds" */
public class TimerValues {
  private static final String EMPTY = "N/A";
  private static final String HOURS = "hours";
  private static final String MINUTES = "minutes";
  private static final String SECONDS = "seconds";
  private int mHours;
  private int mMinutes;
  private int mSeconds;

  /**
   * Creates a {@link TimerValues}
   *
   * @param hours The number of hours to represent
   * @param minutes The number of minutes to represent
   * @param seconds The number of seconds to represent
   */
  public TimerValues(int hours, int minutes, int seconds) {
    checkArgument(hours >= 0, "Hours is negative: %s", hours);
    checkArgument(minutes >= 0, "Minutes is negative: %s", minutes);
    checkArgument(seconds >= 0, "Seconds is negative: %s", seconds);

    mHours = hours;
    mMinutes = minutes;
    mSeconds = seconds;

    normalizeValues();
  }

  /**
   * Creates a {@link TimerValues}
   *
   * @param milliseconds The number of milliseconds to represent
   */
  public TimerValues(long milliseconds) {
    this(
        0 /* hours */,
        0 /* minutes */,
        (int) TimeUnit.SECONDS.convert(milliseconds, TimeUnit.MILLISECONDS));
  }

  /** Creates a {@link TimerValues} from a {@link Bundle} */
  public static TimerValues fromBundle(Bundle bundle) {
    checkArgument(bundle != null, "Bundle is null");

    return new TimerValues(
        bundle.getInt(HOURS, 0), bundle.getInt(MINUTES, 0), bundle.getInt(SECONDS, 0));
  }

  /** Returns a {@link Bundle} from the {@link TimerValues} */
  public Bundle toBundle() {
    Bundle content = new Bundle();
    content.putInt(HOURS, mHours);
    content.putInt(MINUTES, mMinutes);
    content.putInt(SECONDS, mSeconds);

    return content;
  }

  /**
   * Configures a {@link NumberPicker} with appropriate bounds and initial value for displaying
   * "Hours"
   */
  public void configureHours(NumberPicker picker) {
    picker.setMinValue(0);
    picker.setMaxValue((int) TimeUnit.HOURS.convert(1, TimeUnit.DAYS) - 1);
    picker.setValue(mHours);
  }

  /**
   * Configures a {@link NumberPicker} with appropriate bounds and initial value for displaying
   * "Minutes"
   */
  public void configureMinutes(NumberPicker picker) {
    picker.setMinValue(0);
    picker.setMaxValue((int) TimeUnit.MINUTES.convert(1, TimeUnit.HOURS) - 1);
    picker.setValue(mMinutes);
  }

  /**
   * Configures a {@link NumberPicker} with appropriate bounds and initial value for displaying
   * "Seconds"
   */
  public void configureSeconds(NumberPicker picker) {
    picker.setMinValue(0);
    picker.setMaxValue((int) TimeUnit.SECONDS.convert(1, TimeUnit.MINUTES) - 1);
    picker.setValue(mSeconds);
  }

  /** Returns the {@link TimerValues} in milliseconds */
  public long getTotalMilliseconds() {
    return (TimeUnit.MILLISECONDS.convert(mHours, TimeUnit.HOURS)
        + TimeUnit.MILLISECONDS.convert(mMinutes, TimeUnit.MINUTES)
        + TimeUnit.MILLISECONDS.convert(mSeconds, TimeUnit.SECONDS));
  }

  /** Returns {@code true} if {@link TimerValues} is zero. */
  public boolean isZero() {
    return ((mHours == 0) && (mMinutes == 0) && (mSeconds == 0));
  }

  /** Returns string representation that includes "00:00:00" */
  public String toCountdownString() {
    return String.format("%02d:%02d:%02d", mHours, mMinutes, mSeconds);
  }

  /** Normalize seconds and minutes */
  private void normalizeValues() {
    long minuteOverflow = TimeUnit.MINUTES.convert(mSeconds, TimeUnit.SECONDS);
    long hourOverflow = TimeUnit.HOURS.convert(mMinutes, TimeUnit.MINUTES);

    // Apply overflow
    mMinutes += minuteOverflow;
    mHours += hourOverflow;

    // Apply bounds
    mSeconds -= TimeUnit.SECONDS.convert(minuteOverflow, TimeUnit.MINUTES);
    mMinutes -= TimeUnit.MINUTES.convert(hourOverflow, TimeUnit.HOURS);
  }

  @Override
  public String toString() {
    if (isZero()) {
      return EMPTY;
    } else {
      return toCountdownString();
    }
  }
}

```

`app/src/main/java/com/google/android/apps/location/gps/gnsslogger/UiLogger.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.apps.location.gps.gnsslogger;

import android.graphics.Color;
import android.location.GnssClock;
import android.location.GnssMeasurement;
import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.Location;
import android.location.LocationProvider;
import android.os.Bundle;
import android.util.Log;
import com.google.android.apps.location.gps.gnsslogger.LoggerFragment.UIFragmentComponent;
import java.text.DecimalFormat;

/**
 * A class representing a UI logger for the application. Its responsibility is show information in
 * the UI.
 */
public class UiLogger implements MeasurementListener {

  private static final int USED_COLOR = Color.rgb(0x4a, 0x5f, 0x70);

  public UiLogger() {}

  private UIFragmentComponent mUiFragmentComponent;

  public synchronized UIFragmentComponent getUiFragmentComponent() {
    return mUiFragmentComponent;
  }

  public synchronized void setUiFragmentComponent(UIFragmentComponent value) {
    mUiFragmentComponent = value;
  }

  @Override
  public void onProviderEnabled(String provider) {
    logLocationEvent("onProviderEnabled: " + provider);
  }

  @Override
  public void onTTFFReceived(long l) {}

  @Override
  public void onProviderDisabled(String provider) {
    logLocationEvent("onProviderDisabled: " + provider);
  }

  @Override
  public void onLocationChanged(Location location) {
    logLocationEvent("onLocationChanged: " + location + "\n");
  }

  @Override
  public void onLocationStatusChanged(String provider, int status, Bundle extras) {
    String message =
        String.format(
            "onStatusChanged: provider=%s, status=%s, extras=%s",
            provider, locationStatusToString(status), extras);
    logLocationEvent(message);
  }

  @Override
  public void onGnssMeasurementsReceived(GnssMeasurementsEvent event) {
    StringBuilder builder = new StringBuilder("[ GnssMeasurementsEvent:\n\n");

    builder.append(toStringClock(event.getClock()));
    builder.append("\n");

    for (GnssMeasurement measurement : event.getMeasurements()) {
      builder.append(toStringMeasurement(measurement));
      builder.append("\n");
    }

    builder.append("]");
    logMeasurementEvent("onGnssMeasurementsReceived: " + builder.toString());
  }

  private String toStringClock(GnssClock gnssClock) {
    final String format = "   %-4s = %s\n";
    StringBuilder builder = new StringBuilder("GnssClock:\n");
    DecimalFormat numberFormat = new DecimalFormat("#0.000");
    if (gnssClock.hasLeapSecond()) {
      builder.append(String.format(format, "LeapSecond", gnssClock.getLeapSecond()));
    }

    builder.append(String.format(format, "TimeNanos", gnssClock.getTimeNanos()));
    if (gnssClock.hasTimeUncertaintyNanos()) {
      builder.append(
          String.format(format, "TimeUncertaintyNanos", gnssClock.getTimeUncertaintyNanos()));
    }

    if (gnssClock.hasFullBiasNanos()) {
      builder.append(String.format(format, "FullBiasNanos", gnssClock.getFullBiasNanos()));
    }

    if (gnssClock.hasBiasNanos()) {
      builder.append(String.format(format, "BiasNanos", gnssClock.getBiasNanos()));
    }
    if (gnssClock.hasBiasUncertaintyNanos()) {
      builder.append(
          String.format(
              format,
              "BiasUncertaintyNanos",
              numberFormat.format(gnssClock.getBiasUncertaintyNanos())));
    }

    if (gnssClock.hasDriftNanosPerSecond()) {
      builder.append(
          String.format(
              format,
              "DriftNanosPerSecond",
              numberFormat.format(gnssClock.getDriftNanosPerSecond())));
    }

    if (gnssClock.hasDriftUncertaintyNanosPerSecond()) {
      builder.append(
          String.format(
              format,
              "DriftUncertaintyNanosPerSecond",
              numberFormat.format(gnssClock.getDriftUncertaintyNanosPerSecond())));
    }

    builder.append(
        String.format(
            format,
            "HardwareClockDiscontinuityCount",
            gnssClock.getHardwareClockDiscontinuityCount()));

    return builder.toString();
  }

  private String toStringMeasurement(GnssMeasurement measurement) {
    final String format = "   %-4s = %s\n";
    StringBuilder builder = new StringBuilder("GnssMeasurement:\n");
    DecimalFormat numberFormat = new DecimalFormat("#0.000");
    DecimalFormat numberFormat1 = new DecimalFormat("#0.000E00");
    builder.append(String.format(format, "Svid", measurement.getSvid()));
    builder.append(String.format(format, "ConstellationType", measurement.getConstellationType()));
    builder.append(String.format(format, "TimeOffsetNanos", measurement.getTimeOffsetNanos()));

    builder.append(String.format(format, "State", measurement.getState()));

    builder.append(
        String.format(format, "ReceivedSvTimeNanos", measurement.getReceivedSvTimeNanos()));
    builder.append(
        String.format(
            format,
            "ReceivedSvTimeUncertaintyNanos",
            measurement.getReceivedSvTimeUncertaintyNanos()));

    builder.append(String.format(format, "Cn0DbHz", numberFormat.format(measurement.getCn0DbHz())));

    builder.append(
        String.format(
            format,
            "PseudorangeRateMetersPerSecond",
            numberFormat.format(measurement.getPseudorangeRateMetersPerSecond())));
    builder.append(
        String.format(
            format,
            "PseudorangeRateUncertaintyMetersPerSeconds",
            numberFormat.format(measurement.getPseudorangeRateUncertaintyMetersPerSecond())));

    if (measurement.getAccumulatedDeltaRangeState() != GnssMeasurement.ADR_STATE_UNKNOWN) {
      builder.append(
          String.format(
              format, "AccumulatedDeltaRangeState", measurement.getAccumulatedDeltaRangeState()));

      builder.append(
          String.format(
              format,
              "AccumulatedDeltaRangeMeters",
              numberFormat.format(measurement.getAccumulatedDeltaRangeMeters())));
      builder.append(
          String.format(
              format,
              "AccumulatedDeltaRangeUncertaintyMeters",
              numberFormat1.format(measurement.getAccumulatedDeltaRangeUncertaintyMeters())));
    }

    if (measurement.hasCarrierFrequencyHz()) {
      builder.append(
          String.format(format, "CarrierFrequencyHz", measurement.getCarrierFrequencyHz()));
    }

    if (measurement.hasCarrierCycles()) {
      builder.append(String.format(format, "CarrierCycles", measurement.getCarrierCycles()));
    }

    if (measurement.hasCarrierPhase()) {
      builder.append(String.format(format, "CarrierPhase", measurement.getCarrierPhase()));
    }

    if (measurement.hasCarrierPhaseUncertainty()) {
      builder.append(
          String.format(
              format, "CarrierPhaseUncertainty", measurement.getCarrierPhaseUncertainty()));
    }

    builder.append(
        String.format(format, "MultipathIndicator", measurement.getMultipathIndicator()));

    if (measurement.hasSnrInDb()) {
      builder.append(String.format(format, "SnrInDb", measurement.getSnrInDb()));
    }

    if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
      if (measurement.hasAutomaticGainControlLevelDb()) {
        builder.append(
            String.format(format, "AgcDb", measurement.getAutomaticGainControlLevelDb()));
      }
      if (measurement.hasCarrierFrequencyHz()) {
        builder.append(String.format(format, "CarrierFreqHz", measurement.getCarrierFrequencyHz()));
      }
    }

    return builder.toString();
  }

  @Override
  public void onGnssMeasurementsStatusChanged(int status) {
    logMeasurementEvent("onStatusChanged: " + gnssMeasurementsStatusToString(status));
  }

  @Override
  public void onGnssNavigationMessageReceived(GnssNavigationMessage event) {
    logNavigationMessageEvent("onGnssNavigationMessageReceived: " + event);
  }

  @Override
  public void onGnssNavigationMessageStatusChanged(int status) {
    logNavigationMessageEvent("onStatusChanged: " + getGnssNavigationMessageStatus(status));
  }

  @Override
  public void onGnssStatusChanged(GnssStatus gnssStatus) {
    logStatusEvent("onGnssStatusChanged: " + gnssStatusToString(gnssStatus));
  }

  @Override
  public void onNmeaReceived(long timestamp, String s) {
    logNmeaEvent(String.format("onNmeaReceived: timestamp=%d, %s", timestamp, s));
  }

  @Override
  public void onListenerRegistration(String listener, boolean result) {
    logEvent("Registration", String.format("add%sListener: %b", listener, result), USED_COLOR);
  }

  private void logMeasurementEvent(String event) {
    logEvent("Measurement", event, USED_COLOR);
  }

  private void logNavigationMessageEvent(String event) {
    logEvent("NavigationMsg", event, USED_COLOR);
  }

  private void logStatusEvent(String event) {
    logEvent("Status", event, USED_COLOR);
  }

  private void logNmeaEvent(String event) {
    logEvent("Nmea", event, USED_COLOR);
  }

  private void logEvent(String tag, String message, int color) {
    String composedTag = MeasurementProvider.TAG + tag;
    Log.d(composedTag, message);
    logText(tag, message, color);
  }

  private void logText(String tag, String text, int color) {
    UIFragmentComponent component = getUiFragmentComponent();
    if (component != null) {
      component.logTextFragment(tag, text, color);
    }
  }

  private String locationStatusToString(int status) {
    switch (status) {
      case LocationProvider.AVAILABLE:
        return "AVAILABLE";
      case LocationProvider.OUT_OF_SERVICE:
        return "OUT_OF_SERVICE";
      case LocationProvider.TEMPORARILY_UNAVAILABLE:
        return "TEMPORARILY_UNAVAILABLE";
      default:
        return "<Unknown>";
    }
  }

  private String gnssMeasurementsStatusToString(int status) {
    switch (status) {
      case GnssMeasurementsEvent.Callback.STATUS_NOT_SUPPORTED:
        return "NOT_SUPPORTED";
      case GnssMeasurementsEvent.Callback.STATUS_READY:
        return "READY";
      case GnssMeasurementsEvent.Callback.STATUS_LOCATION_DISABLED:
        return "GNSS_LOCATION_DISABLED";
      default:
        return "<Unknown>";
    }
  }

  private String getGnssNavigationMessageStatus(int status) {
    switch (status) {
      case GnssNavigationMessage.STATUS_UNKNOWN:
        return "Status Unknown";
      case GnssNavigationMessage.STATUS_PARITY_PASSED:
        return "READY";
      case GnssNavigationMessage.STATUS_PARITY_REBUILT:
        return "Status Parity Rebuilt";
      default:
        return "<Unknown>";
    }
  }

  private String gnssStatusToString(GnssStatus gnssStatus) {

    StringBuilder builder = new StringBuilder("SATELLITE_STATUS | [Satellites:\n");
    for (int i = 0; i < gnssStatus.getSatelliteCount(); i++) {
      builder
          .append("Constellation = ")
          .append(getConstellationName(gnssStatus.getConstellationType(i)))
          .append(", ");
      builder.append("Svid = ").append(gnssStatus.getSvid(i)).append(", ");
      builder.append("Cn0DbHz = ").append(gnssStatus.getCn0DbHz(i)).append(", ");
      builder.append("Elevation = ").append(gnssStatus.getElevationDegrees(i)).append(", ");
      builder.append("Azimuth = ").append(gnssStatus.getAzimuthDegrees(i)).append(", ");
      builder.append("hasEphemeris = ").append(gnssStatus.hasEphemerisData(i)).append(", ");
      builder.append("hasAlmanac = ").append(gnssStatus.hasAlmanacData(i)).append(", ");
      builder.append("usedInFix = ").append(gnssStatus.usedInFix(i)).append("\n");
    }
    builder.append("]");
    return builder.toString();
  }

  private void logLocationEvent(String event) {
    logEvent("Location", event, USED_COLOR);
  }

  private String getConstellationName(int id) {
    switch (id) {
      case 1:
        return "GPS";
      case 2:
        return "SBAS";
      case 3:
        return "GLONASS";
      case 4:
        return "QZSS";
      case 5:
        return "BEIDOU";
      case 6:
        return "GALILEO";
      default:
        return "UNKNOWN";
    }
  }
}

```

`app/src/main/res/layout/activity_main.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <com.google.android.material.tabs.TabLayout
        android:id="@+id/tab_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

    <androidx.viewpager.widget.ViewPager
        android:id="@+id/pager"
        android:layout_width="match_parent"
        android:layout_height="fill_parent"
        android:layout_below="@id/tab_layout"/>

</LinearLayout>
```

`app/src/main/res/layout/fragment_agnss.xml`:

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    android:paddingBottom="@dimen/activity_vertical_margin"
    tools:context=".MainActivity">

 <LinearLayout
        android:orientation="horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
        <Button
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="@string/clearAgps"
            android:layout_marginTop="0dp"
            android:id="@+id/clearAgps"
            android:singleLine="true" />
       <Button
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="@string/fetchExtraData"
            android:layout_marginTop="0dp"
            android:id="@+id/fetchExtraData"
            android:singleLine="true" />
        <Button
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="@string/fetchTimeData"
            android:layout_marginTop="0dp"
            android:id="@+id/fetchTimeData"
            android:singleLine="true" />
    </LinearLayout>

    <LinearLayout
        android:orientation="horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
         <Button
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="@string/requestSingleNlp"
            android:layout_marginTop="0dp"
            android:id="@+id/requestSingleNlp"
            android:textSize="10.5sp"
            android:singleLine="true" />
        <Button
            android:id="@+id/clear_log"
            android:layout_marginTop="0dp"
            android:text="Clear"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content" />
        <Button
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="@string/requestSingleGps"
            android:layout_marginTop="0dp"
            android:id="@+id/requestSingleGps"
            android:singleLine="true" />
    </LinearLayout>

     <ScrollView
        android:id="@+id/log_scroll"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1">

    <TextView
        android:id="@+id/log_view"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

    </ScrollView>

</LinearLayout>
```

`app/src/main/res/layout/fragment_log.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical" >

    <LinearLayout
        android:orientation="horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <Button
            android:id="@+id/start_log"
            android:text="\u2770 Start"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content" />
        <Button
            android:id="@+id/clear_log"
            android:text="Clear"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content" />
        <Button
            android:id="@+id/end_log"
            android:text="End \u2771"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <ScrollView
        android:id="@+id/log_scroll"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1">
        <TextView
            android:id="@+id/log_view"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </ScrollView>

    <LinearLayout
        android:orientation="horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
      <TextView
          android:id="@+id/timer_display"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:layout_weight="1"
          android:gravity="center_horizontal"
          android:textStyle="bold" />

    </LinearLayout>

    <LinearLayout
        android:orientation="horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
        <Button
            android:id="@+id/timer"
            android:text="Timer"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"/>

        <Button
            android:id="@+id/start_logs"
            android:text="Start Log"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"/>

        <Button
            android:id="@+id/send_file"
            android:text="Stop &amp; Send"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"/>

    </LinearLayout>

</LinearLayout>

```

`app/src/main/res/layout/fragment_main.xml`:

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/setting_root"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    android:paddingBottom="@dimen/activity_vertical_margin"
    tools:context=".MainActivity">

  <LinearLayout
      android:orientation="horizontal"
      android:layout_width="match_parent"
      android:layout_height="wrap_content">
    <TextView
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:layout_marginTop="15dp"
        android:id="@+id/register_location_label" />
    <Switch
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:id="@+id/register_location"
        android:singleLine="true"
        android:layout_marginTop="15dp"
        android:text="@string/location_label" />
  </LinearLayout>

  <LinearLayout
      android:orientation="horizontal"
      android:layout_width="match_parent"
      android:layout_height="wrap_content">
    <TextView
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:layout_marginTop="15dp"
        android:id="@+id/register_measurement_label" />
    <Switch
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:id="@+id/register_measurements"
        android:singleLine="true"
        android:layout_marginTop="15dp"
        android:text="@string/measurements_label" />
  </LinearLayout>

  <LinearLayout
      android:orientation="horizontal"
      android:layout_width="match_parent"
      android:layout_height="wrap_content">
    <TextView
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:layout_gravity="center_vertical"
        android:textStyle="bold"
        android:layout_marginTop="15dp"
        android:id="@+id/register_navigation_label" />
    <Switch
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:id="@+id/register_navigation"
        android:singleLine="true"
        android:layout_marginTop="15dp"
        android:text="@string/nav_msg_label" />
  </LinearLayout>

  <LinearLayout
      android:orientation="horizontal"
      android:layout_width="match_parent"
      android:layout_height="wrap_content">
    <TextView
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:layout_marginTop="15dp"
        android:id="@+id/register_status_label" />
    <Switch
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:id="@+id/register_status"
        android:singleLine="true"
        android:layout_marginTop="15dp"
        android:text="@string/gnss_status_label" />
  </LinearLayout>

  <LinearLayout
      android:orientation="horizontal"
      android:layout_width="match_parent"
      android:layout_height="wrap_content">
    <TextView
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:layout_marginTop="15dp"
        android:id="@+id/register_nmea_label" />
    <Switch
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:id="@+id/register_nmea"
        android:singleLine="true"
        android:layout_marginTop="15dp"
        android:text="@string/nmea_label" />
  </LinearLayout>

  <LinearLayout
      android:orientation="horizontal"
      android:layout_width="match_parent"
      android:layout_height="wrap_content">
    <TextView
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:layout_marginTop="15dp"
        android:id="@+id/turn_on_auto_scroll" />
    <Switch
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:id="@+id/auto_scroll_on"
        android:singleLine="true"
        android:layout_marginTop="15dp"
        android:text="@string/auto_scroll" />
  </LinearLayout>

  <LinearLayout
      android:orientation="horizontal"
      android:layout_width="match_parent"
      android:layout_height="wrap_content">
    <TextView
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:layout_marginTop="15dp"
        android:id="@+id/turn_on_residual_plot" />
    <Switch
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_height="wrap_content"
        android:id="@+id/residual_plot_enabled"
        android:singleLine="true"
        android:layout_marginTop="15dp"
        android:text="@string/residual_plot" />
  </LinearLayout>

  <RelativeLayout
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:orientation="vertical">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_above="@+id/sw_and_info"
        android:orientation="horizontal">

      <Button
          android:id="@+id/help"
          android:layout_width="0dp"
          android:layout_height="wrap_content"
          android:layout_weight="1"
          android:singleLine="true"
          android:text="@string/help" />

      <Button
          android:id="@+id/exit"
          android:layout_width="0dp"
          android:layout_height="wrap_content"
          android:layout_weight="1"
          android:singleLine="true"
          android:text="@string/exit" />
    </LinearLayout>

    <LinearLayout
        android:id="@+id/sw_and_info"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:layout_gravity="bottom"
        android:orientation="horizontal">

      <TextView
          android:id="@+id/sw_info"
          android:layout_width="0dp"
          android:layout_height="wrap_content"
          android:layout_weight="1"
          android:gravity="start|bottom"
          android:textStyle="bold" />

      <TextView
          android:layout_width="0dp"
          android:layout_height="wrap_content"
          android:layout_weight="1"
          android:gravity="end|bottom"
          android:text="@string/app_version"
          android:textStyle="italic|bold" />
    </LinearLayout>
  </RelativeLayout>


</LinearLayout>
```

`app/src/main/res/layout/fragment_plot.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
  <LinearLayout
      android:layout_width="match_parent"
      android:layout_height="0dp"
      android:orientation="vertical"
      android:id="@+id/plot"
      android:layout_weight="3">
  </LinearLayout>
  <LinearLayout
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:orientation = "horizontal">
    <Spinner
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:gravity="start"
        android:id = "@+id/constellation_spinner"
        android:entries="@array/constellation_arrays">
    </Spinner>
    <Spinner
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:gravity="end"
        android:id = "@+id/tab_spinner"
        android:entries="@array/tab_arrays">
    </Spinner>
  </LinearLayout>
  <TextView
      android:layout_width="match_parent"
      android:layout_height="0dp"
      android:id="@+id/analysis"
      android:text="@string/turn_on_location_measurement"
      android:layout_weight="1"/>
</LinearLayout>
```

`app/src/main/res/layout/help.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical" >

    <android.webkit.WebView
        android:id="@+id/helpView"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content" >
    </android.webkit.WebView>

</LinearLayout>
```

`app/src/main/res/layout/map_fragment.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
  android:orientation="vertical"
  android:layout_width="match_parent"
  android:layout_height="match_parent">
  <com.google.android.gms.maps.MapView
    android:id="@+id/map"
    android:layout_width="match_parent"
    android:layout_height="0dp"
    android:layout_weight="9" />

</LinearLayout>
```

`app/src/main/res/layout/pop_up_window.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:background="@color/background_material_light"
    android:id="@+id/pop">
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="@dimen/abc_text_size_title_material_toolbar"
        android:textColor="@color/background_material_dark"
        android:text="@string/please_select_ground_truth_mode"/>
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
      <TextView
          android:layout_width="0dp"
          android:layout_weight="1"
          android:layout_height="wrap_content"
          android:gravity="start"
          android:text="@string/ground_solution_mode"/>
      <Spinner
          android:layout_width="0dp"
          android:layout_weight="1"
          android:layout_height="wrap_content"
          android:gravity="end"
          android:id="@+id/residual_spinner"
          android:entries="@array/residual_options"
          android:spinnerMode="dialog">
      </Spinner>
    </LinearLayout>
    <EditText
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:id="@+id/latitude_input"
      android:inputType="numberDecimal|numberSigned"
      android:hint="@string/latitude_in_degrees"/>
    <EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/longitude_input"
        android:inputType="numberDecimal|numberSigned"
        android:hint="@string/longitude_in_degrees"/>
    <EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/altitude_input"
        android:inputType="numberDecimal|numberSigned"
        android:hint="@string/altitude_in_meters"/>
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">
      <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:id="@+id/popup_button_ok"
          android:text="@string/ok"/>
      <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:id="@+id/popup_button_cancel"
          android:text="@string/cancel"/>
    </LinearLayout>
</LinearLayout>
```

`app/src/main/res/layout/results_log.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical" >

    <LinearLayout
        android:orientation="horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <Button
            android:id="@+id/start_log"
            android:text="\u2770 Start"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content" />
        <Button
            android:id="@+id/clear_log"
            android:text="Clear"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content" />
        <Button
            android:id="@+id/end_log"
            android:text="End \u2771"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <ScrollView
        android:id="@+id/log_scroll"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1">

        <TextView
            android:id="@+id/log_view"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </ScrollView>

</LinearLayout>

```

`app/src/main/res/layout/timer.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- Center landmark -->
    <RelativeLayout
        android:id="@+id/minutes_container"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerVertical="true"
        android:layout_centerHorizontal="true">
        <NumberPicker
            android:id="@+id/minutes_picker"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_centerVertical="true"/>
        <TextView
            android:id="@+id/minutes_text"
            android:text="@string/timer_minutes"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_centerHorizontal="true"
            android:layout_below="@id/minutes_picker"/>

    </RelativeLayout>

    <RelativeLayout
        android:id="@+id/hours_container"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_toLeftOf="@id/minutes_container">
        <NumberPicker
            android:id="@+id/hours_picker"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_centerVertical="true"/>
        <TextView
            android:id="@+id/hours_text"
            android:text="@string/timer_hours"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_centerHorizontal="true"
            android:layout_below="@id/hours_picker"/>

    </RelativeLayout>

    <RelativeLayout
        android:id="@+id/seconds_container"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_toRightOf="@+id/minutes_container">
        <NumberPicker
            android:id="@+id/seconds_picker"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_centerVertical="true"/>
        <TextView
            android:id="@+id/seconds_text"
            android:text="@string/timer_seconds"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_centerHorizontal="true"
            android:layout_below="@+id/seconds_picker"/>

    </RelativeLayout>

</RelativeLayout>

```

`app/src/main/res/raw/help_contents.txt`:

```txt
<a href="#about_apphelp">About AppHelp</a>
<br>
<a href="#feedback">Feedback</a>
<br>
<a name="about_apphelp" id="about_apphelp">
<h3>About AppHelp</h3>
<ul>
  <li>Start Log button: Starts logging when pushed.</li>
  <li>Stop & Send button: Stops logging and shows dialog to send the file via email or other options.</li>  
</ul>

</a>
<br>
<a name="feedback" id="feedback">
<h3>Feedback</h3>
Any comments, feedback, suggestions on GNSSLogger please write to us using the link below.
<br>
<a href="mailto:pseudoranges-feedback@google.com">Contact support</a>
</a>
<br>
```

`app/src/main/res/values-w820dp/dimens.xml`:

```xml
<resources>
    <!-- Example customization of dimensions originally defined in res/values/dimens.xml
         (such as screen margins) for screens with more than 820dp of available width. This
         would include 7" and 10" devices in landscape (~960dp and ~1280dp respectively). -->
    <dimen name="activity_horizontal_margin">64dp</dimen>
</resources>

```

`app/src/main/res/values/colors.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="colorPrimary">#3F51B5</color>
    <color name="colorPrimaryDark">#303F9F</color>
    <color name="colorAccent">#FF4081</color>
</resources>

```

`app/src/main/res/values/dimens.xml`:

```xml
<resources>
    <!-- Default screen margins, per the Android Design guidelines. -->
    <dimen name="activity_horizontal_margin">16dp</dimen>
    <dimen name="activity_vertical_margin">16dp</dimen>
    <dimen name="button_text_size">12sp</dimen>
</resources>

```

`app/src/main/res/values/strings.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">
    <string name="app_name">GnssLogger</string>
    <string name="app_version">v2.0.0.1</string>

    <string name="title_settings">Settings</string>
    <string name="title_log">Log</string>
    <string name="title_offset">Position Offset</string>
    <string name="title_map">Map</string>
    <string name="title_agnss">AGNSS</string>
    <string name="title_device">Device</string>
    <string name="title_wls">WLS</string>
    <string name="title_plot">Plot</string>

    <string name="location_label">Location</string>
    <string name="measurements_label">Measurements</string>
    <string name="nav_msg_label">Navigation Messages</string>
    <string name="gnss_status_label">GnssStatus</string>
    <string name="nmea_label">Nmea</string>
    <string name="auto_scroll">Auto Scroll</string>
    <string name="residual_plot">Residual Plot</string>

    <string name="help">HELP</string>
    <string name="exit">Exit</string>
    <string name="clearAgps">Clear AGPS</string>
    <string name="fetchExtraData">Get Xtra</string>
    <string name="fetchTimeData">Inject Time</string>
    <string name="requestSingleNlp">Get Network Loc.</string>
    <string name="requestSingleGps">Get GPS Loc.</string>
    <string name="ttff">TTFF</string>

    <string name="timer_service_name">GNSS Logger timer</string>
    <string name="timer_service_notification_channel_name">name</string>
    <string name="timer_service_notification_channel_description">description</string>
    <string name="timer_title">Timer Settings</string>
    <string name="timer_hours">Hours</string>
    <string name="timer_minutes">Minutes</string>
    <string name="timer_seconds">Seconds</string>
    <string name="timer_set">Set</string>
    <string name="timer_reset">Reset</string>
    <string name="timer_cancel">Cancel</string>
    <string name="timer_display">Time Remaining</string>
    <string name="start_message">Starting log...</string>
    <string name="stop_message">Sending file...</string>
    <string name="longitude_in_degrees">Longitude in decimal degrees</string>
    <string name="ground_solution_mode">Ground Truth Mode:</string>
    <string name="please_select_ground_truth_mode">Please Select Ground Truth Mode</string>
    <string name="latitude_in_degrees">Latitude in decimal degrees</string>
    <string name="altitude_in_meters">Altitude in meters</string>
    <string name="turn_on_location_measurement">
        No Measurement has been received yet. Please turn on Measurement and Location in Settings.
    </string>
    <string name="ok">OK</string>
    <string name="cancel">Cancel</string>
    <string name="current_average_hint">Current Average Of Strongest 4 Satellites:
        <xliff:g id="currentAverage">%s</xliff:g></string>
    <string name="history_average_hint">History Average of Strongest 4 Satellites:
        <xliff:g id="historyAverage">%s</xliff:g></string>
    <string name="satellite_number_sum_hint">Total Number of Visible Satellites:
        <xliff:g id="totalNumber">%d</xliff:g></string>
    <string-array name="constellation_arrays">
        <item>All</item>
        <item>GPS</item>
        <item>SBAS</item>
        <item>GLONASS</item>
        <item>QZSS</item>
        <item>BEIDOU</item>
        <item>GALILEO</item>
    </string-array>
    <string-array name="tab_arrays">
        <item>C/N0</item>
        <item>PR Residual</item>
    </string-array>
    <string-array name="residual_options">
        <item>Manual - Still</item>
        <item>Manual - Moving</item>
        <item>Manual - Use LLA input</item>
        <item>Automatic - AR Based</item>
    </string-array>
    <string-array name="plot_titles">
        <item>CN0(dB.Hz) vs Time(s)</item>
        <item>Pseudorange residual(m) vs Time(s)</item>
    </string-array>
</resources>

```

`app/src/main/res/values/styles.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="Theme.AppCompat.Light.DarkActionBar">
    </style>
</resources>

```

`app/src/main/res/xml/file_providers_paths.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <external-path name="external_files" path="."/>
</paths>
```

`app/src/test/java/com/google/android/apps/location/gps/gnsslogger/ExampleUnitTest.java`:

```java
package com.google.android.apps.location.gps.gnsslogger;

import static org.junit.Assert.*;

import org.junit.Test;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
  @Test
  public void addition_isCorrect() {
    assertEquals(4, 2 + 2);
  }
}

```

`build.gradle`:

```gradle
// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    id 'com.android.application' version '7.2.1' apply false
    id 'com.android.library' version '7.2.1' apply false
    id 'com.google.android.libraries.mapsplatform.secrets-gradle-plugin' version '2.0.1' apply false
    id 'com.github.sherter.google-java-format' version '0.9'
}

task clean(type: Delete) {
    delete rootProject.buildDir
}

```

`gradle.properties`:

```properties
# Project-wide Gradle settings.
# IDE (e.g. Android Studio) users:
# Gradle settings configured through the IDE *will override*
# any settings specified in this file.
# For more details on how to configure your build environment visit
# http://www.gradle.org/docs/current/userguide/build_environment.html
# Specifies the JVM arguments used for the daemon process.
# The setting is particularly useful for tweaking memory settings.
org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
# When configured, Gradle will run in incubating parallel mode.
# This option should only be used with decoupled projects. More details, visit
# http://www.gradle.org/docs/current/userguide/multi_project_builds.html#sec:decoupled_projects
# org.gradle.parallel=true
# AndroidX package structure to make it clearer which packages are bundled with the
# Android operating system, and which are packaged with your app"s APK
# https://developer.android.com/topic/libraries/support-library/androidx-rn
android.useAndroidX=true
# Enables namespacing of each library's R class so that its R class includes only the
# resources declared in the library itself and none from the library's dependencies,
# thereby reducing the size of the R class for that library
android.nonTransitiveRClass=true
android.enableJetifier=true
```

`gradle/wrapper/gradle-wrapper.properties`:

```properties
#Sat Jul 02 10:53:35 GMT+08:00 2022
distributionBase=GRADLE_USER_HOME
distributionUrl=https\://services.gradle.org/distributions/gradle-7.3.3-bin.zip
distributionPath=wrapper/dists
zipStorePath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME

```

`gradlew`:

```
#!/usr/bin/env sh

#
# Copyright 2015 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

##############################################################################
##
##  Gradle start up script for UN*X
##
##############################################################################

# Attempt to set APP_HOME
# Resolve links: $0 may be a link
PRG="$0"
# Need this for relative symlinks.
while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
        PRG="$link"
    else
        PRG=`dirname "$PRG"`"/$link"
    fi
done
SAVED="`pwd`"
cd "`dirname \"$PRG\"`/" >/dev/null
APP_HOME="`pwd -P`"
cd "$SAVED" >/dev/null

APP_NAME="Gradle"
APP_BASE_NAME=`basename "$0"`

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS='"-Xmx64m" "-Xms64m"'

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD="maximum"

warn () {
    echo "$*"
}

die () {
    echo
    echo "$*"
    echo
    exit 1
}

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "`uname`" in
  CYGWIN* )
    cygwin=true
    ;;
  Darwin* )
    darwin=true
    ;;
  MINGW* )
    msys=true
    ;;
  NONSTOP* )
    nonstop=true
    ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar


# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD="$JAVA_HOME/jre/sh/java"
    else
        JAVACMD="$JAVA_HOME/bin/java"
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD="java"
    which java >/dev/null 2>&1 || die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
fi

# Increase the maximum file descriptors if we can.
if [ "$cygwin" = "false" -a "$darwin" = "false" -a "$nonstop" = "false" ] ; then
    MAX_FD_LIMIT=`ulimit -H -n`
    if [ $? -eq 0 ] ; then
        if [ "$MAX_FD" = "maximum" -o "$MAX_FD" = "max" ] ; then
            MAX_FD="$MAX_FD_LIMIT"
        fi
        ulimit -n $MAX_FD
        if [ $? -ne 0 ] ; then
            warn "Could not set maximum file descriptor limit: $MAX_FD"
        fi
    else
        warn "Could not query maximum file descriptor limit: $MAX_FD_LIMIT"
    fi
fi

# For Darwin, add options to specify how the application appears in the dock
if $darwin; then
    GRADLE_OPTS="$GRADLE_OPTS \"-Xdock:name=$APP_NAME\" \"-Xdock:icon=$APP_HOME/media/gradle.icns\""
fi

# For Cygwin or MSYS, switch paths to Windows format before running java
if [ "$cygwin" = "true" -o "$msys" = "true" ] ; then
    APP_HOME=`cygpath --path --mixed "$APP_HOME"`
    CLASSPATH=`cygpath --path --mixed "$CLASSPATH"`

    JAVACMD=`cygpath --unix "$JAVACMD"`

    # We build the pattern for arguments to be converted via cygpath
    ROOTDIRSRAW=`find -L / -maxdepth 1 -mindepth 1 -type d 2>/dev/null`
    SEP=""
    for dir in $ROOTDIRSRAW ; do
        ROOTDIRS="$ROOTDIRS$SEP$dir"
        SEP="|"
    done
    OURCYGPATTERN="(^($ROOTDIRS))"
    # Add a user-defined pattern to the cygpath arguments
    if [ "$GRADLE_CYGPATTERN" != "" ] ; then
        OURCYGPATTERN="$OURCYGPATTERN|($GRADLE_CYGPATTERN)"
    fi
    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    i=0
    for arg in "$@" ; do
        CHECK=`echo "$arg"|egrep -c "$OURCYGPATTERN" -`
        CHECK2=`echo "$arg"|egrep -c "^-"`                                 ### Determine if an option

        if [ $CHECK -ne 0 ] && [ $CHECK2 -eq 0 ] ; then                    ### Added a condition
            eval `echo args$i`=`cygpath --path --ignore --mixed "$arg"`
        else
            eval `echo args$i`="\"$arg\""
        fi
        i=`expr $i + 1`
    done
    case $i in
        0) set -- ;;
        1) set -- "$args0" ;;
        2) set -- "$args0" "$args1" ;;
        3) set -- "$args0" "$args1" "$args2" ;;
        4) set -- "$args0" "$args1" "$args2" "$args3" ;;
        5) set -- "$args0" "$args1" "$args2" "$args3" "$args4" ;;
        6) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" ;;
        7) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" ;;
        8) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" ;;
        9) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" "$args8" ;;
    esac
fi

# Escape application args
save () {
    for i do printf %s\\n "$i" | sed "s/'/'\\\\''/g;1s/^/'/;\$s/\$/' \\\\/" ; done
    echo " "
}
APP_ARGS=`save "$@"`

# Collect all arguments for the java command, following the shell quoting and substitution rules
eval set -- $DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS "\"-Dorg.gradle.appname=$APP_BASE_NAME\"" -classpath "\"$CLASSPATH\"" org.gradle.wrapper.GradleWrapperMain "$APP_ARGS"

exec "$JAVACMD" "$@"

```

`gradlew.bat`:

```bat
@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS="-Xmx64m" "-Xms64m"

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto execute

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %*

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%GRADLE_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega

```

`local.defaults.properties`:

```properties
## This file is a sample for how to writing local.properties.
# Do not modify this file -- YOUR CHANGES WILL BE ERASED!
#
# This file should *NOT* be checked into Version Control Systems,
# as it contains information specific to your local configuration.
#
# Location of the SDK. This is only used by Gradle.
# For customization when using a Version Control System, please read the
# header note.
sdk.dir=C\:\\Users\\username\\AppData\\Local\\Android\\Sdk
MAPS_API_KEY=GoogleMapsApiKey

```

`pseudorange/build.gradle`:

```gradle
plugins {
    id 'com.android.library'
}

android {
    compileSdk 32

    defaultConfig {
        minSdk 24
        targetSdk 32

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
        consumerProguardFiles "consumer-rules.pro"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {

    implementation 'joda-time:joda-time:2.9.4'
    implementation 'androidx.appcompat:appcompat:1.4.2'
    implementation 'junit:junit:4.12'
    implementation files('libs/commons-math3-3.6.1.jar')
    implementation 'com.google.android.gms:play-services-location:11.0.2'
    implementation files('libs/commons-codec-1.10.jar')
    implementation files('libs/asn1-supl2.jar')
    implementation files('libs/asn1-base.jar')
    implementation files('libs/suplClient.jar')
    implementation files('libs/protobuf-nano.jar')
    implementation("com.google.guava:guava:31.1-android")
    
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
}

```

`pseudorange/proguard-rules.pro`:

```pro
# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

# Uncomment this to preserve the line number information for
# debugging stack traces.
#-keepattributes SourceFile,LineNumberTable

# If you keep the line number information, uncomment this to
# hide the original source file name.
#-renamesourcefileattribute SourceFile
```

`pseudorange/src/androidTest/java/com/google/android/apps/location/gps/gnsslogger/pseudorange/ExampleInstrumentedTest.java`:

```java
package com.google.android.apps.location.gps.gnsslogger.pseudorange;

import static org.junit.Assert.*;

import android.content.Context;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.platform.app.InstrumentationRegistry;
import org.junit.Test;
import org.junit.runner.RunWith;

/**
 * Instrumented test, which will execute on an Android device.
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
@RunWith(AndroidJUnit4.class)
public class ExampleInstrumentedTest {
  @Test
  public void useAppContext() {
    // Context of the app under test.
    Context appContext = InstrumentationRegistry.getInstrumentation().getTargetContext();
    assertEquals(
        "com.google.location.lbs.gnss.gps.pseudorange.test",
        appContext.getPackageName());
  }
}

```

`pseudorange/src/main/AndroidManifest.xml`:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.google.location.lbs.gnss.gps.pseudorange">

</manifest>

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/Ecef2EnuConverter.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealMatrix;

/**
 * Converts ECEF (Earth Centered Earth Fixed) Cartesian coordinates to local ENU (East, North, and
 * Up).
 *
 * <p>Source: reference from Navipedia:
 * http://www.navipedia.net/index.php/Transformations_between_ECEF_and_ENU_coordinates
 */
public class Ecef2EnuConverter {

  /**
   * Converts a vector represented by coordinates ecefX, ecefY, ecefZ in an Earth-Centered
   * Earth-Fixed (ECEF) Cartesian system into a vector in a local east-north-up (ENU) Cartesian
   * system.
   *
   * <p>For example it can be used to rotate a speed vector or position offset vector to ENU.
   *
   * @param ecefX X coordinates in ECEF
   * @param ecefY Y coordinates in ECEF
   * @param ecefZ Z coordinates in ECEF
   * @param refLat Latitude in Radians of the Reference Position
   * @param refLng Longitude in Radians of the Reference Position
   * @return the converted values in {@code EnuValues}
   */
  public static EnuValues convertEcefToEnu(
      double ecefX, double ecefY, double ecefZ, double refLat, double refLng) {

    RealMatrix rotationMatrix = getRotationMatrix(refLat, refLng);
    RealMatrix ecefCoordinates = new Array2DRowRealMatrix(new double[] {ecefX, ecefY, ecefZ});

    RealMatrix enuResult = rotationMatrix.multiply(ecefCoordinates);
    return new EnuValues(
        enuResult.getEntry(0, 0), enuResult.getEntry(1, 0), enuResult.getEntry(2, 0));
  }

  /**
   * Computes a rotation matrix for converting a vector in Earth-Centered Earth-Fixed (ECEF)
   * Cartesian system into a vector in local east-north-up (ENU) Cartesian system with respect to a
   * reference location. The matrix has the following content:
   *
   * <p>- sinLng cosLng 0 - sinLat * cosLng - sinLat * sinLng cosLat cosLat * cosLng cosLat * sinLng
   * sinLat
   *
   * <p>Reference: Pratap Misra and Per Enge "Global Positioning System: Signals, Measurements, and
   * Performance" Page 137.
   *
   * @param refLat Latitude of reference location
   * @param refLng Longitude of reference location
   * @return the Ecef to Enu rotation matrix
   */
  public static RealMatrix getRotationMatrix(double refLat, double refLng) {
    RealMatrix rotationMatrix = new Array2DRowRealMatrix(3, 3);

    // Fill in the rotation Matrix
    rotationMatrix.setEntry(0, 0, -1 * Math.sin(refLng));
    rotationMatrix.setEntry(1, 0, -1 * Math.cos(refLng) * Math.sin(refLat));
    rotationMatrix.setEntry(2, 0, Math.cos(refLng) * Math.cos(refLat));
    rotationMatrix.setEntry(0, 1, Math.cos(refLng));
    rotationMatrix.setEntry(1, 1, -1 * Math.sin(refLat) * Math.sin(refLng));
    rotationMatrix.setEntry(2, 1, Math.cos(refLat) * Math.sin(refLng));
    rotationMatrix.setEntry(0, 2, 0);
    rotationMatrix.setEntry(1, 2, Math.cos(refLat));
    rotationMatrix.setEntry(2, 2, Math.sin(refLat));
    return rotationMatrix;
  }

  /** A container for values in ENU (East, North, Up) coordination system. */
  public static class EnuValues {

    /** East Coordinates in local ENU */
    public final double enuEast;

    /** North Coordinates in local ENU */
    public final double enuNorth;

    /** Up Coordinates in local ENU */
    public final double enuUP;

    /** Constructor */
    public EnuValues(double enuEast, double enuNorth, double enuUP) {
      this.enuEast = enuEast;
      this.enuNorth = enuNorth;
      this.enuUP = enuUP;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/Ecef2LlaConverter.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

/**
 * Converts ECEF (Earth Centered Earth Fixed) Cartesian coordinates to LLA (latitude, longitude, and
 * altitude).
 *
 * <p>Source: reference from Mathworks: https://microem.ru/files/2012/08/GPS.G1-X-00006.pdf
 * http://www.mathworks.com/help/aeroblks/ecefpositiontolla.html
 */
public class Ecef2LlaConverter {
  // WGS84 Ellipsoid Parameters
  private static final double EARTH_SEMI_MAJOR_AXIS_METERS = 6378137.0;
  private static final double ECCENTRICITY = 8.1819190842622e-2;
  private static final double INVERSE_FLATTENING = 298.257223563;
  private static final double MIN_MAGNITUDE_METERS = 1.0e-22;
  private static final double MAX_ITERATIONS = 15;
  private static final double RESIDUAL_TOLERANCE = 1.0e-6;
  private static final double SEMI_MINOR_AXIS_METERS =
      Math.sqrt(Math.pow(EARTH_SEMI_MAJOR_AXIS_METERS, 2) * (1 - Math.pow(ECCENTRICITY, 2)));
  private static final double SECOND_ECCENTRICITY =
      Math.sqrt(
          (Math.pow(EARTH_SEMI_MAJOR_AXIS_METERS, 2) - Math.pow(SEMI_MINOR_AXIS_METERS, 2))
              / Math.pow(SEMI_MINOR_AXIS_METERS, 2));
  private static final double ECEF_NEAR_POLE_THRESHOLD_METERS = 1.0;

  /**
   * Converts ECEF (Earth Centered Earth Fixed) Cartesian coordinates to LLA (latitude, longitude,
   * and altitude) using the close form approach
   *
   * <p>Inputs are cartesian coordinates x,y,z
   *
   * <p>Output is GeodeticLlaValues class containing geodetic latitude (radians), geodetic longitude
   * (radians), height above WGS84 ellipsoid (m)}
   */
  public static GeodeticLlaValues convertECEFToLLACloseForm(
      double ecefXMeters, double ecefYMeters, double ecefZMeters) {

    // Auxiliary parameters
    double pMeters = Math.sqrt(Math.pow(ecefXMeters, 2) + Math.pow(ecefYMeters, 2));
    double thetaRadians =
        Math.atan2(EARTH_SEMI_MAJOR_AXIS_METERS * ecefZMeters, SEMI_MINOR_AXIS_METERS * pMeters);

    double lngRadians = Math.atan2(ecefYMeters, ecefXMeters);
    // limit longitude to range of 0 to 2Pi
    lngRadians = lngRadians % (2 * Math.PI);

    final double sinTheta = Math.sin(thetaRadians);
    final double cosTheta = Math.cos(thetaRadians);
    final double tempY =
        ecefZMeters
            + Math.pow(SECOND_ECCENTRICITY, 2) * SEMI_MINOR_AXIS_METERS * Math.pow(sinTheta, 3);
    final double tempX =
        pMeters
            - Math.pow(ECCENTRICITY, 2) * EARTH_SEMI_MAJOR_AXIS_METERS * (Math.pow(cosTheta, 3));
    double latRadians = Math.atan2(tempY, tempX);
    // Radius of curvature in the vertical prime
    double curvatureRadius =
        EARTH_SEMI_MAJOR_AXIS_METERS
            / Math.sqrt(1 - Math.pow(ECCENTRICITY, 2) * (Math.pow(Math.sin(latRadians), 2)));
    double altMeters = (pMeters / Math.cos(latRadians)) - curvatureRadius;

    // Correct for numerical instability in altitude near poles
    boolean polesCheck =
        Math.abs(ecefXMeters) < ECEF_NEAR_POLE_THRESHOLD_METERS
            && Math.abs(ecefYMeters) < ECEF_NEAR_POLE_THRESHOLD_METERS;
    if (polesCheck) {
      altMeters = Math.abs(ecefZMeters) - SEMI_MINOR_AXIS_METERS;
    }

    return new GeodeticLlaValues(latRadians, lngRadians, altMeters);
  }

  /**
   * Converts ECEF (Earth Centered Earth Fixed) Cartesian coordinates to LLA (latitude, longitude,
   * and altitude) using iteration approach
   *
   * <p>Inputs are cartesian coordinates x,y,z.
   *
   * <p>Outputs is GeodeticLlaValues containing geodetic latitude (radians), geodetic longitude
   * (radians), height above WGS84 ellipsoid (m)}
   */
  public static GeodeticLlaValues convertECEFToLLAByIterations(
      double ecefXMeters, double ecefYMeters, double ecefZMeters) {

    double xyLengthMeters = Math.sqrt(Math.pow(ecefXMeters, 2) + Math.pow(ecefYMeters, 2));
    double xyzLengthMeters = Math.sqrt(Math.pow(xyLengthMeters, 2) + Math.pow(ecefZMeters, 2));

    double lngRad;
    if (xyLengthMeters > MIN_MAGNITUDE_METERS) {
      lngRad = Math.atan2(ecefYMeters, ecefXMeters);
    } else {
      lngRad = 0;
    }

    double sinPhi;
    if (xyzLengthMeters > MIN_MAGNITUDE_METERS) {
      sinPhi = ecefZMeters / xyzLengthMeters;
    } else {
      sinPhi = 0;
    }
    // initial latitude (iterate next to improve accuracy)
    double latRad = Math.asin(sinPhi);
    double altMeters;
    if (xyzLengthMeters > MIN_MAGNITUDE_METERS) {
      double ni;
      double pResidual;
      double ecefZMetersResidual;
      // initial height (iterate next to improve accuracy)
      altMeters =
          xyzLengthMeters
              - EARTH_SEMI_MAJOR_AXIS_METERS * (1 - sinPhi * sinPhi / INVERSE_FLATTENING);

      for (int i = 1; i <= MAX_ITERATIONS; i++) {
        sinPhi = Math.sin(latRad);

        // calculate radius of curvature in prime vertical direction
        ni =
            EARTH_SEMI_MAJOR_AXIS_METERS
                / Math.sqrt(
                    1
                        - (2 - 1 / INVERSE_FLATTENING)
                            / INVERSE_FLATTENING
                            * Math.sin(latRad)
                            * Math.sin(latRad));

        // calculate residuals in p and ecefZMeters
        pResidual = xyLengthMeters - (ni + altMeters) * Math.cos(latRad);
        ecefZMetersResidual =
            ecefZMeters
                - (ni * (1 - (2 - 1 / INVERSE_FLATTENING) / INVERSE_FLATTENING) + altMeters)
                    * Math.sin(latRad);

        // update height and latitude
        altMeters += Math.sin(latRad) * ecefZMetersResidual + Math.cos(latRad) * pResidual;
        latRad +=
            (Math.cos(latRad) * ecefZMetersResidual - Math.sin(latRad) * pResidual)
                / (ni + altMeters);

        if (Math.sqrt((pResidual * pResidual + ecefZMetersResidual * ecefZMetersResidual))
            < RESIDUAL_TOLERANCE) {
          break;
        }

        if (i == MAX_ITERATIONS) {
          System.err.println(
              "Geodetic coordinate calculation did not converge in " + i + " iterations");
        }
      }
    } else {
      altMeters = 0;
    }
    return new GeodeticLlaValues(latRad, lngRad, altMeters);
  }

  /**
   * Class containing geodetic coordinates: latitude in radians, geodetic longitude in radians and
   * altitude in meters
   */
  public static class GeodeticLlaValues {

    public final double latitudeRadians;
    public final double longitudeRadians;
    public final double altitudeMeters;

    public GeodeticLlaValues(
        double latitudeRadians, double longitudeRadians, double altitudeMeters) {
      this.latitudeRadians = latitudeRadians;
      this.longitudeRadians = longitudeRadians;
      this.altitudeMeters = altitudeMeters;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/EcefToTopocentricConverter.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import com.google.location.lbs.gnss.gps.pseudorange.Ecef2LlaConverter.GeodeticLlaValues;
import org.apache.commons.math3.linear.RealMatrix;

/** Transformations from ECEF coordinates to Topocentric coordinates */
public class EcefToTopocentricConverter {
  private static final double MIN_DISTANCE_MAGNITUDE_METERS = 1.0e-22;
  private static final int EAST_IDX = 0;
  private static final int NORTH_IDX = 1;
  private static final int UP_IDX = 2;

  /**
   * Transformation of {@code inputVectorMeters} with origin at {@code originECEFMeters} into
   * topocentric coordinate system. The result is {@code TopocentricAEDValues} containing azimuth
   * from north +ve clockwise, radians; elevation angle, radians; distance, vector length meters
   *
   * <p>Source: http://www.navipedia.net/index.php/Transformations_between_ECEF_and_ENU_coordinates
   * http://kom.aau.dk/~borre/life-l99/topocent.m
   */
  public static TopocentricAEDValues convertCartesianToTopocentricRadMeters(
      final double[] originECEFMeters, final double[] inputVectorMeters) {

    GeodeticLlaValues latLngAlt =
        Ecef2LlaConverter.convertECEFToLLACloseForm(
            originECEFMeters[0], originECEFMeters[1], originECEFMeters[2]);

    RealMatrix rotationMatrix =
        Ecef2EnuConverter.getRotationMatrix(latLngAlt.latitudeRadians, latLngAlt.longitudeRadians)
            .transpose();
    double[] eastNorthUpVectorMeters =
        GpsMathOperations.matrixByColVectMultiplication(
            rotationMatrix.transpose().getData(), inputVectorMeters);
    double eastMeters = eastNorthUpVectorMeters[EAST_IDX];
    double northMeters = eastNorthUpVectorMeters[NORTH_IDX];
    double upMeters = eastNorthUpVectorMeters[UP_IDX];

    // calculate azimuth, elevation and height from the ENU values
    double horizontalDistanceMeters = Math.hypot(eastMeters, northMeters);
    double azimuthRadians;
    double elevationRadians;

    if (horizontalDistanceMeters < MIN_DISTANCE_MAGNITUDE_METERS) {
      elevationRadians = Math.PI / 2.0;
      azimuthRadians = 0;
    } else {
      elevationRadians = Math.atan2(upMeters, horizontalDistanceMeters);
      azimuthRadians = Math.atan2(eastMeters, northMeters);
    }
    if (azimuthRadians < 0) {
      azimuthRadians += 2 * Math.PI;
    }

    double distanceMeters =
        Math.sqrt(
            Math.pow(inputVectorMeters[0], 2)
                + Math.pow(inputVectorMeters[1], 2)
                + Math.pow(inputVectorMeters[2], 2));
    return new TopocentricAEDValues(elevationRadians, azimuthRadians, distanceMeters);
  }

  /**
   * Calculates azimuth, elevation in radians,and distance in meters between the user position in
   * ECEF meters {@code userPositionECEFMeters} and the satellite position in ECEF meters {@code
   * satPositionECEFMeters}
   */
  public static TopocentricAEDValues calculateElAzDistBetween2Points(
      double[] userPositionECEFMeters, double[] satPositionECEFMeters) {

    return convertCartesianToTopocentricRadMeters(
        userPositionECEFMeters,
        GpsMathOperations.subtractTwoVectors(satPositionECEFMeters, userPositionECEFMeters));
  }

  /**
   * Class containing topocenter coordinates: azimuth in radians, elevation in radians, and distance
   * in meters
   */
  public static class TopocentricAEDValues {

    public final double elevationRadians;
    public final double azimuthRadians;
    public final double distanceMeters;

    public TopocentricAEDValues(
        double elevationRadians, double azimuthRadians, double distanceMeters) {
      this.elevationRadians = elevationRadians;
      this.azimuthRadians = azimuthRadians;
      this.distanceMeters = distanceMeters;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/ElevationApiHelper.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import static java.nio.charset.StandardCharsets.UTF_8;

import com.google.common.base.Preconditions;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * A helper class to access the Google Elevation API for computing the Terrain Elevation Above Sea
 * level at a given location (lat, lng). An Elevation API key is required for getting elevation
 * above sea level from Google server.
 *
 * <p>For more information please see:
 * https://developers.google.com/maps/documentation/elevation/start
 *
 * <p>A key can be conveniently acquired from:
 * https://developers.google.com/maps/documentation/elevation/get-api-key
 */
public class ElevationApiHelper {

  private static final String ELEVATION_XML_STRING = "<elevation>";
  private static final String GOOGLE_ELEVATION_API_HTTP_ADDRESS =
      "https://maps.googleapis.com/maps/api/elevation/xml?locations=";
  private String elevationApiKey = "";

  /**
   * A constructor that passes the {@code elevationApiKey}. If the user pass an empty string for API
   * Key, an {@code IllegalArgumentException} will be thrown.
   */
  public ElevationApiHelper(String elevationApiKey) {
    // An Elevation API key must be provided for getting elevation from Google Server.
    Preconditions.checkArgument(!elevationApiKey.isEmpty());
    this.elevationApiKey = elevationApiKey;
  }

  /**
   * Calculates the geoid height by subtracting the elevation above sea level from the ellipsoid
   * height in altitude meters.
   */
  public static double calculateGeoidHeightMeters(
      double altitudeMeters, double elevationAboveSeaLevelMeters) {
    return altitudeMeters - elevationAboveSeaLevelMeters;
  }

  /**
   * Gets elevation (height above sea level) via the Google elevation API by requesting elevation
   * for a given latitude and longitude. Longitude and latitude should be in decimal degrees and the
   * returned elevation will be in meters.
   */
  public double getElevationAboveSeaLevelMeters(double latitudeDegrees, double longitudeDegrees)
      throws Exception {

    String url =
        GOOGLE_ELEVATION_API_HTTP_ADDRESS
            + latitudeDegrees
            + ","
            + longitudeDegrees
            + "&key="
            + elevationApiKey;
    String elevationMeters = "0.0";

    HttpURLConnection urlConnection = (HttpURLConnection) new URL(url).openConnection();
    InputStream content = urlConnection.getInputStream();
    BufferedReader buffer = new BufferedReader(new InputStreamReader(content, UTF_8));
    String line;
    while ((line = buffer.readLine()) != null) {
      line = line.trim();
      if (line.startsWith(ELEVATION_XML_STRING)) {
        // read the part of the line after the opening tag <elevation>
        String substring = line.substring(ELEVATION_XML_STRING.length(), line.length());
        // read the part of the line until before the closing tag <elevation>
        elevationMeters =
            substring.substring(0, substring.length() - ELEVATION_XML_STRING.length() - 1);
      }
    }
    return Double.parseDouble(elevationMeters);
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/GpsMathOperations.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import java.util.Arrays;

/**
 * Helper class containing the basic vector and matrix operations used for calculating the position
 * solution from pseudoranges
 */
public class GpsMathOperations {

  /** Calculates the norm of a vector */
  public static double vectorNorm(double[] inputVector) {
    double normSquared = 0;
    for (int i = 0; i < inputVector.length; i++) {
      normSquared = Math.pow(inputVector[i], 2) + normSquared;
    }

    return Math.sqrt(normSquared);
  }

  /**
   * Subtract two vectors {@code firstVector} - {@code secondVector}. Both vectors should be of the
   * same length.
   */
  public static double[] subtractTwoVectors(double[] firstVector, double[] secondVector)
      throws ArithmeticException {
    double[] result = new double[firstVector.length];
    if (firstVector.length != secondVector.length) {
      throw new ArithmeticException("Input vectors are of different lengths");
    }

    for (int i = 0; i < firstVector.length; i++) {
      result[i] = firstVector[i] - secondVector[i];
    }

    return result;
  }

  /**
   * Multiply a matrix {@code matrix} by a column vector {@code vector} ({@code matrix} * {@code
   * vector}) and return the resulting vector {@resultVector}. {@code matrix} and {@resultVector}
   * dimensions must match.
   */
  public static double[] matrixByColVectMultiplication(double[][] matrix, double[] resultVector)
      throws ArithmeticException {
    double[] result = new double[matrix.length];
    int matrixLength = matrix.length;
    int vectorLength = resultVector.length;
    if (vectorLength != matrix[0].length) {
      throw new ArithmeticException("Matrix and vector dimensions do not match");
    }

    for (int i = 0; i < matrixLength; i++) {
      for (int j = 0; j < vectorLength; j++) {
        result[i] += matrix[i][j] * resultVector[j];
      }
    }

    return result;
  }

  /**
   * Dot product of a raw vector {@code firstVector} and a column vector {@code secondVector}. Both
   * vectors should be of the same length.
   */
  public static double dotProduct(double[] firstVector, double[] secondVector)
      throws ArithmeticException {
    if (firstVector.length != secondVector.length) {
      throw new ArithmeticException("Input vectors are of different lengths");
    }
    double result = 0;
    for (int i = 0; i < firstVector.length; i++) {
      result = firstVector[i] * secondVector[i] + result;
    }
    return result;
  }

  /**
   * Finds the index of max value in a vector {@code vector} filtering out NaNs, return -1 if the
   * vector is empty or only contain NaNs.
   */
  public static int maxIndexOfVector(double[] vector) {
    double max = Double.NEGATIVE_INFINITY;
    int index = -1;

    for (int i = 0; i < vector.length; i++) {
      if (!Double.isNaN(vector[i])) {
        if (vector[i] > max) {
          index = i;
          max = vector[i];
        }
      }
    }

    return index;
  }

  /**
   * Subtracts every element in a vector {@code vector} by a scalar {@code scalar}. We do not need
   * to filter out NaN in this case because NaN subtract by a real number will still be NaN.
   */
  public static double[] subtractByScalar(double[] vector, double scalar) {
    double[] result = new double[vector.length];

    for (int i = 0; i < vector.length; i++) {
      result[i] = vector[i] - scalar;
    }

    return result;
  }

  /**
   * Computes the mean value of a vector {@code vector}, filtering out NaNs. If no non-NaN exists,
   * return Double.NaN {@link Double#NaN}
   */
  public static double meanOfVector(double[] vector) {
    double sum = 0;
    double size = 0;

    for (int i = 0; i < vector.length; i++) {
      if (!Double.isNaN(vector[i])) {
        sum += vector[i];
        size++;
      }
    }
    return size == 0 ? Double.NaN : sum / size;
  }

  /** Creates a numeric array of size {@code size} and fills it with the value {@code value} */
  public static double[] createAndFillArray(int size, double value) {
    double[] vector = new double[size];

    Arrays.fill(vector, value);

    return vector;
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/GpsMeasurement.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

/**
 * A container for the received GPS measurements for a single satellite.
 *
 * <p>The GPS receiver measurements includes: satellite PRN, accumulated delta range in meters,
 * accumulated delta range state (boolean), pseudorange rate in meters per second, received signal
 * to noise ratio dB, accumulated delta range uncertainty in meters, pseudorange rate uncertainty in
 * meters per second.
 */
class GpsMeasurement {
  /** Time since GPS week start (Nano seconds) */
  public final long arrivalTimeSinceGpsWeekNs;

  /** Accumulated delta range (meters) */
  public final double accumulatedDeltaRangeMeters;

  /** Accumulated delta range state */
  public final boolean validAccumulatedDeltaRangeMeters;

  /** Pseudorange rate measurement (meters per second) */
  public final double pseudorangeRateMps;

  /** Signal to noise ratio (dB) */
  public final double signalToNoiseRatioDb;

  /** Accumulated Delta Range Uncertainty (meters) */
  public final double accumulatedDeltaRangeUncertaintyMeters;

  /** Pseudorange rate uncertainty (meter per seconds) */
  public final double pseudorangeRateUncertaintyMps;

  public GpsMeasurement(
      long arrivalTimeSinceGpsWeekNs,
      double accumulatedDeltaRangeMeters,
      boolean validAccumulatedDeltaRangeMeters,
      double pseudorangeRateMps,
      double signalToNoiseRatioDb,
      double accumulatedDeltaRangeUncertaintyMeters,
      double pseudorangeRateUncertaintyMps) {
    this.arrivalTimeSinceGpsWeekNs = arrivalTimeSinceGpsWeekNs;
    this.accumulatedDeltaRangeMeters = accumulatedDeltaRangeMeters;
    this.validAccumulatedDeltaRangeMeters = validAccumulatedDeltaRangeMeters;
    this.pseudorangeRateMps = pseudorangeRateMps;
    this.signalToNoiseRatioDb = signalToNoiseRatioDb;
    this.accumulatedDeltaRangeUncertaintyMeters = accumulatedDeltaRangeUncertaintyMeters;
    this.pseudorangeRateUncertaintyMps = pseudorangeRateUncertaintyMps;
  }

  protected GpsMeasurement(GpsMeasurement another) {
    this(
        another.arrivalTimeSinceGpsWeekNs,
        another.accumulatedDeltaRangeMeters,
        another.validAccumulatedDeltaRangeMeters,
        another.pseudorangeRateMps,
        another.signalToNoiseRatioDb,
        another.accumulatedDeltaRangeUncertaintyMeters,
        another.pseudorangeRateUncertaintyMps);
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/GpsMeasurementWithRangeAndUncertainty.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

/**
 * A container for the received GPS measurements for a single satellite.
 *
 * <p>The container extends {@link GpsMeasurement} to additionally include {@link
 * #pseudorangeMeters} and {@link #pseudorangeUncertaintyMeters}.
 */
class GpsMeasurementWithRangeAndUncertainty extends GpsMeasurement {

  /** Pseudorange measurement (meters) */
  public final double pseudorangeMeters;

  /** Pseudorange uncertainty (meters) */
  public final double pseudorangeUncertaintyMeters;

  public GpsMeasurementWithRangeAndUncertainty(
      GpsMeasurement another, double pseudorangeMeters, double pseudorangeUncertaintyMeters) {
    super(another);
    this.pseudorangeMeters = pseudorangeMeters;
    this.pseudorangeUncertaintyMeters = pseudorangeUncertaintyMeters;
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/GpsNavigationMessageStore.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import android.location.cts.nano.Ephemeris.GpsEphemerisProto;
import android.location.cts.nano.Ephemeris.GpsNavMessageProto;
import android.location.cts.nano.Ephemeris.IonosphericModelProto;
import androidx.annotation.NonNull;
import com.google.common.base.Preconditions;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

/**
 * A class to extract the fields of the GPS navigation message from the raw bytes received from the
 * GPS receiver.
 *
 * <p>Raw bytes are passed by calling the method {@link #onNavMessageReported(byte, byte, short,
 * byte[])}
 *
 * <p>A {@link GpsNavMessageProto} containing the extracted field is obtained by calling the method
 * {@link #createDecodedNavMessage()}
 *
 * <p>References: http://www.gps.gov/technical/icwg/IS-GPS-200D.pdf and
 * http://www.gps.gov/technical/ps/1995-SPS-signal-specification.pdf
 */
public class GpsNavigationMessageStore {

  private static final byte IONOSPHERIC_PARAMETERS_PAGE_18_SV_ID = 56;

  private static final int WORD_SIZE_BITS = 30;
  private static final int WORD_PADDING_BITS = 2;
  private static final int BYTE_AS_BITS = 8;
  private static final int GPS_CYCLE_WEEKS = 1024;
  private static final int IODE_TO_IODC_MASK = 0xFF;

  public static final int SUBFRAME_1 = (1 << 0);
  public static final int SUBFRAME_2 = (1 << 1);
  public static final int SUBFRAME_3 = (1 << 2);
  public static final int SUBFRAME_4 = (1 << 3);
  public static final int SUBFRAME_5 = (1 << 4);

  private static final double POW_2_4 = Math.pow(2, 4);
  private static final double POW_2_11 = Math.pow(2, 11);
  private static final double POW_2_12 = Math.pow(2, 12);
  private static final double POW_2_14 = Math.pow(2, 14);
  private static final double POW_2_16 = Math.pow(2, 16);
  private static final double POW_2_NEG_5 = Math.pow(2, -5);
  private static final double POW_2_NEG_19 = Math.pow(2, -19);
  private static final double POW_2_NEG_24 = Math.pow(2, -24);
  private static final double POW_2_NEG_27 = Math.pow(2, -27);
  private static final double POW_2_NEG_29 = Math.pow(2, -29);
  private static final double POW_2_NEG_30 = Math.pow(2, -30);
  private static final double POW_2_NEG_31 = Math.pow(2, -31);
  private static final double POW_2_NEG_33 = Math.pow(2, -33);
  private static final double POW_2_NEG_43 = Math.pow(2, -43);
  private static final double POW_2_NEG_55 = Math.pow(2, -55);

  private static final long INTEGER_RANGE = 0xFFFFFFFFL;
  // 3657 is the number of days between the unix epoch and GPS epoch as the GPS epoch started on
  // Jan 6, 1980
  private static final long GPS_EPOCH_AS_UNIX_EPOCH_MS = TimeUnit.DAYS.toMillis(3657);
  // A GPS Cycle is 1024 weeks, or 7168 days
  private static final long GPS_CYCLE_MS = TimeUnit.DAYS.toMillis(7168);

  /** Maximum possible number of GPS satellites */
  public static final int MAX_NUMBER_OF_SATELLITES = 32;

  private static final int L1_CA_MESSAGE_LENGTH_BYTES = 40;

  private static final int IODC1_INDEX = 82;
  private static final int IODC1_LENGTH = 2;
  private static final int IODC2_INDEX = 210;
  private static final int IODC2_LENGTH = 8;
  private static final int WEEK_INDEX = 60;
  private static final int WEEK_LENGTH = 10;
  private static final int URA_INDEX = 72;
  private static final int URA_LENGTH = 4;
  private static final int SV_HEALTH_INDEX = 76;
  private static final int SV_HEALTH_LENGTH = 6;
  private static final int TGD_INDEX = 196;
  private static final int TGD_LENGTH = 8;
  private static final int AF2_INDEX = 240;
  private static final int AF2_LENGTH = 8;
  private static final int AF1_INDEX = 248;
  private static final int AF1_LENGTH = 16;
  private static final int AF0_INDEX = 270;
  private static final int AF0_LENGTH = 22;
  private static final int IODE1_INDEX = 60;
  private static final int IODE_LENGTH = 8;
  private static final int TOC_INDEX = 218;
  private static final int TOC_LENGTH = 16;
  private static final int CRS_INDEX = 68;
  private static final int CRS_LENGTH = 16;
  private static final int DELTA_N_INDEX = 90;
  private static final int DELTA_N_LENGTH = 16;
  private static final int M0_INDEX8 = 106;
  private static final int M0_INDEX24 = 120;
  private static final int CUC_INDEX = 150;
  private static final int CUC_LENGTH = 16;
  private static final int E_INDEX8 = 166;
  private static final int E_INDEX24 = 180;
  private static final int CUS_INDEX = 210;
  private static final int CUS_LENGTH = 16;
  private static final int A_INDEX8 = 226;
  private static final int A_INDEX24 = 240;
  private static final int TOE_INDEX = 270;
  private static final int TOE_LENGTH = 16;
  private static final int IODE2_INDEX = 270;
  private static final int CIC_INDEX = 60;
  private static final int CIC_LENGTH = 16;
  private static final int O0_INDEX8 = 76;
  private static final int O0_INDEX24 = 90;
  private static final int O_INDEX8 = 196;
  private static final int O_INDEX24 = 210;
  private static final int ODOT_INDEX = 240;
  private static final int ODOT_LENGTH = 24;
  private static final int CIS_INDEX = 120;
  private static final int CIS_LENGTH = 16;
  private static final int I0_INDEX8 = 136;
  private static final int I0_INDEX24 = 150;
  private static final int CRC_INDEX = 180;
  private static final int CRC_LENGTH = 16;
  private static final int IDOT_INDEX = 278;
  private static final int IDOT_LENGTH = 14;
  private static final int A0_INDEX = 68;
  private static final int A_B_LENGTH = 8;
  private static final int A1_INDEX = 76;
  private static final int A2_INDEX = 90;
  private static final int A3_INDEX = 98;
  private static final int B0_INDEX = 106;
  private static final int B1_INDEX = 120;
  private static final int B2_INDEX = 128;
  private static final int B3_INDEX = 136;
  private static final int WN_LS_INDEX = 226;
  private static final int DELTA_T_LS_INDEX = 240;
  private static final int TOT_LS_INDEX = 218;
  private static final int DN_LS_INDEX = 256;
  private static final int WNF_LS_INDEX = 248;
  private static final int DELTA_TF_LS_INDEX = 270;
  private static final int I0UTC_INDEX8 = 210;
  private static final int I0UTC_INDEX24 = 180;
  private static final int I1UTC_INDEX = 150;

  /** Partially decoded intermediate ephemerides */
  private final IntermediateEphemeris[] partiallyDecodedIntermediateEphemerides =
      new IntermediateEphemeris[MAX_NUMBER_OF_SATELLITES];

  /** Fully decoded intermediate ephemerides */
  private final IntermediateEphemeris[] fullyDecodedIntermediateEphemerides =
      new IntermediateEphemeris[MAX_NUMBER_OF_SATELLITES];

  private IonosphericModelProto decodedIonosphericObj;

  /**
   * Builds and returns the current {@link GpsNavMessageProto} filling the different ephemeris for
   * the different satellites and setting the ionospheric model parameters.
   */
  @NonNull
  public GpsNavMessageProto createDecodedNavMessage() {
    synchronized (fullyDecodedIntermediateEphemerides) {
      ;
      GpsNavMessageProto gpsNavMessageProto = new GpsNavMessageProto();
      ArrayList<GpsEphemerisProto> gpsEphemerisProtoList = new ArrayList<>();
      for (int i = 0; i < MAX_NUMBER_OF_SATELLITES; i++) {
        if (fullyDecodedIntermediateEphemerides[i] != null) {
          gpsEphemerisProtoList.add(fullyDecodedIntermediateEphemerides[i].getEphemerisObj());
        }
      }
      if (decodedIonosphericObj != null) {
        gpsNavMessageProto.iono = decodedIonosphericObj;
      }
      gpsNavMessageProto.ephemerids =
          gpsEphemerisProtoList.toArray(new GpsEphemerisProto[gpsEphemerisProtoList.size()]);
      return gpsNavMessageProto;
    }
  }

  /** Handles a fresh Navigation Message. The message is in its raw format. */
  public void onNavMessageReported(byte prn, byte type, short id, byte[] rawData) {
    Preconditions.checkArgument(type == 1, "Unsupported NavigationMessage Type: " + type);
    Preconditions.checkArgument(
        rawData != null && rawData.length == L1_CA_MESSAGE_LENGTH_BYTES,
        "Invalid length of rawData for L1 C/A");
    synchronized (fullyDecodedIntermediateEphemerides) {
      switch (id) {
        case 1:
          handleFirstSubframe(prn, rawData);
          break;
        case 2:
          handleSecondSubframe(prn, rawData);
          break;
        case 3:
          handleThirdSubframe(prn, rawData);
          break;
        case 4:
          handleFourthSubframe(rawData);
          break;
        case 5:
          break;
        default:
          // invalid message id
          throw new IllegalArgumentException("Invalid Subframe ID: " + id);
      }
    }
  }

  /**
   * Handles the first navigation message subframe which contains satellite clock correction
   * parameters, GPS date (week number) plus satellite status and health.
   */
  private void handleFirstSubframe(byte prn, byte[] rawData) {
    int iodc = extractBits(IODC1_INDEX, IODC1_LENGTH, rawData) << 8;
    iodc |= extractBits(IODC2_INDEX, IODC2_LENGTH, rawData);

    IntermediateEphemeris intermediateEphemeris =
        findIntermediateEphemerisToUpdate(prn, SUBFRAME_1, iodc);
    if (intermediateEphemeris == null) {
      // we are up-to-date
      return;
    }

    GpsEphemerisProto gpsEphemerisProto = intermediateEphemeris.getEphemerisObj();
    gpsEphemerisProto.iodc = iodc;

    // the navigation message contains a modulo-1023 week number
    int week = extractBits(WEEK_INDEX, WEEK_LENGTH, rawData);
    week = getGpsWeekWithRollover(week);
    gpsEphemerisProto.week = week;

    int uraIndex = extractBits(URA_INDEX, URA_LENGTH, rawData);
    double svAccuracy = computeNominalSvAccuracy(uraIndex);
    gpsEphemerisProto.svAccuracyM = svAccuracy;

    int svHealth = extractBits(SV_HEALTH_INDEX, SV_HEALTH_LENGTH, rawData);
    gpsEphemerisProto.svHealth = svHealth;

    byte tgd = (byte) extractBits(TGD_INDEX, TGD_LENGTH, rawData);
    gpsEphemerisProto.tgd = tgd * POW_2_NEG_31;

    int toc = extractBits(TOC_INDEX, TOC_LENGTH, rawData);
    double tocScaled = toc * POW_2_4;
    gpsEphemerisProto.toc = tocScaled;

    byte af2 = (byte) extractBits(AF2_INDEX, AF2_LENGTH, rawData);
    gpsEphemerisProto.af2 = af2 * POW_2_NEG_55;

    short af1 = (short) extractBits(AF1_INDEX, AF1_LENGTH, rawData);
    gpsEphemerisProto.af1 = af1 * POW_2_NEG_43;

    // a 22-bit two's complement number
    int af0 = extractBits(AF0_INDEX, AF0_LENGTH, rawData);
    af0 = getTwoComplement(af0, AF0_LENGTH);
    gpsEphemerisProto.af0 = af0 * POW_2_NEG_31;

    updateDecodedState(prn, SUBFRAME_1, intermediateEphemeris);
  }

  /** Handles the second navigation message subframe which contains satellite ephemeris */
  private void handleSecondSubframe(byte prn, byte[] rawData) {
    int iode = extractBits(IODE1_INDEX, IODE_LENGTH, rawData);

    IntermediateEphemeris intermediateEphemeris =
        findIntermediateEphemerisToUpdate(prn, SUBFRAME_2, iode);
    if (intermediateEphemeris == null) {
      // nothing to update
      return;
    }

    GpsEphemerisProto gpsEphemerisProto = intermediateEphemeris.getEphemerisObj();

    gpsEphemerisProto.iode = iode;

    short crs = (short) extractBits(CRS_INDEX, CRS_LENGTH, rawData);
    gpsEphemerisProto.crs = crs * POW_2_NEG_5;

    short deltaN = (short) extractBits(DELTA_N_INDEX, DELTA_N_LENGTH, rawData);
    gpsEphemerisProto.deltaN = deltaN * POW_2_NEG_43 * Math.PI;

    int m0 = (int) buildUnsigned32BitsWordFrom8And24Words(M0_INDEX8, M0_INDEX24, rawData);
    gpsEphemerisProto.m0 = m0 * POW_2_NEG_31 * Math.PI;

    short cuc = (short) extractBits(CUC_INDEX, CUC_LENGTH, rawData);
    gpsEphemerisProto.cuc = cuc * POW_2_NEG_29;

    // an unsigned 32 bit value
    long e = buildUnsigned32BitsWordFrom8And24Words(E_INDEX8, E_INDEX24, rawData);
    gpsEphemerisProto.e = e * POW_2_NEG_33;

    short cus = (short) extractBits(CUS_INDEX, CUS_LENGTH, rawData);
    gpsEphemerisProto.cus = cus * POW_2_NEG_29;

    // an unsigned 32 bit value
    long a = buildUnsigned32BitsWordFrom8And24Words(A_INDEX8, A_INDEX24, rawData);
    gpsEphemerisProto.rootOfA = a * POW_2_NEG_19;

    int toe = extractBits(TOE_INDEX, TOE_LENGTH, rawData);
    double toeScaled = toe * POW_2_4;
    gpsEphemerisProto.toe = toe * POW_2_4;

    updateDecodedState(prn, SUBFRAME_2, intermediateEphemeris);
  }

  /** Handles the third navigation message subframe which contains satellite ephemeris */
  private void handleThirdSubframe(byte prn, byte[] rawData) {

    int iode = extractBits(IODE2_INDEX, IODE_LENGTH, rawData);

    IntermediateEphemeris intermediateEphemeris =
        findIntermediateEphemerisToUpdate(prn, SUBFRAME_3, iode);
    if (intermediateEphemeris == null) {
      // A fully or partially decoded message is available , hence nothing to update
      return;
    }

    GpsEphemerisProto gpsEphemerisProto = intermediateEphemeris.getEphemerisObj();
    gpsEphemerisProto.iode = iode;

    short cic = (short) extractBits(CIC_INDEX, CIC_LENGTH, rawData);
    gpsEphemerisProto.cic = cic * POW_2_NEG_29;

    int o0 = (int) buildUnsigned32BitsWordFrom8And24Words(O0_INDEX8, O0_INDEX24, rawData);
    gpsEphemerisProto.omega0 = o0 * POW_2_NEG_31 * Math.PI;

    int o = (int) buildUnsigned32BitsWordFrom8And24Words(O_INDEX8, O_INDEX24, rawData);
    gpsEphemerisProto.omega = o * POW_2_NEG_31 * Math.PI;

    int odot = extractBits(ODOT_INDEX, ODOT_LENGTH, rawData);
    odot = getTwoComplement(odot, ODOT_LENGTH);
    ;
    gpsEphemerisProto.omegaDot = odot * POW_2_NEG_43 * Math.PI;

    short cis = (short) extractBits(CIS_INDEX, CIS_LENGTH, rawData);
    gpsEphemerisProto.cis = cis * POW_2_NEG_29;

    int i0 = (int) buildUnsigned32BitsWordFrom8And24Words(I0_INDEX8, I0_INDEX24, rawData);
    gpsEphemerisProto.i0 = i0 * POW_2_NEG_31 * Math.PI;

    short crc = (short) extractBits(CRC_INDEX, CRC_LENGTH, rawData);
    gpsEphemerisProto.crc = crc * POW_2_NEG_5;

    // a 14-bit two's complement number
    int idot = extractBits(IDOT_INDEX, IDOT_LENGTH, rawData);
    idot = getTwoComplement(idot, IDOT_LENGTH);
    gpsEphemerisProto.iDot = idot * POW_2_NEG_43 * Math.PI;

    updateDecodedState(prn, SUBFRAME_3, intermediateEphemeris);
  }

  /**
   * Subframe four provides ionospheric model parameters , UTC information, part of the almanac, and
   * indications whether the Anti-Spoofing, is activated or not.
   *
   * <p>For now, only the ionospheric parameters are parsed.
   */
  private void handleFourthSubframe(byte[] rawData) {
    byte pageId = (byte) extractBits(62, 6, rawData);
    if (pageId != IONOSPHERIC_PARAMETERS_PAGE_18_SV_ID) {
      // We only care to decode ionospheric parameters for now
      return;
    }

    IonosphericModelProto ionosphericModelProto = new IonosphericModelProto();

    double[] alpha = new double[4];
    byte a0 = (byte) extractBits(A0_INDEX, A_B_LENGTH, rawData);
    alpha[0] = a0 * POW_2_NEG_30;
    byte a1 = (byte) extractBits(A1_INDEX, A_B_LENGTH, rawData);
    alpha[1] = a1 * POW_2_NEG_27;
    byte a2 = (byte) extractBits(A2_INDEX, A_B_LENGTH, rawData);
    alpha[2] = a2 * POW_2_NEG_24;
    byte a3 = (byte) extractBits(A3_INDEX, A_B_LENGTH, rawData);
    alpha[3] = a3 * POW_2_NEG_24;
    ionosphericModelProto.alpha = alpha;

    double[] beta = new double[4];
    byte b0 = (byte) extractBits(B0_INDEX, A_B_LENGTH, rawData);
    beta[0] = b0 * POW_2_11;
    byte b1 = (byte) extractBits(B1_INDEX, A_B_LENGTH, rawData);
    beta[1] = b1 * POW_2_14;
    byte b2 = (byte) extractBits(B2_INDEX, A_B_LENGTH, rawData);
    beta[2] = b2 * POW_2_16;
    byte b3 = (byte) extractBits(B3_INDEX, A_B_LENGTH, rawData);
    beta[3] = b3 * POW_2_16;
    ionosphericModelProto.beta = beta;

    double a0UTC =
        buildSigned32BitsWordFrom8And24WordsWith8bitslsb(I0UTC_INDEX8, I0UTC_INDEX24, rawData)
            * Math.pow(2, -30);

    double a1UTC = getTwoComplement(extractBits(I1UTC_INDEX, 24, rawData), 24) * Math.pow(2, -50);

    short tot = (short) (extractBits(TOT_LS_INDEX, A_B_LENGTH, rawData) * POW_2_12);

    short wnt = (short) extractBits(WN_LS_INDEX, A_B_LENGTH, rawData);

    short tls = (short) extractBits(DELTA_T_LS_INDEX, A_B_LENGTH, rawData);

    short wnlsf = (short) extractBits(WNF_LS_INDEX, A_B_LENGTH, rawData);

    short dn = (short) extractBits(DN_LS_INDEX, A_B_LENGTH, rawData);

    short tlsf = (short) extractBits(DELTA_TF_LS_INDEX, A_B_LENGTH, rawData);

    decodedIonosphericObj = ionosphericModelProto;
  }

  /**
   * Updates the {@link IntermediateEphemeris} with the decoded status of the current subframe.
   * Moreover, update the {@code partiallyDecodedIntermediateEphemerides} list and {@code
   * fullyDecodedIntermediateEphemerides} list
   */
  private void updateDecodedState(
      byte prn, int decodedSubframeNumber, IntermediateEphemeris intermediateEphemeris) {
    intermediateEphemeris.reportDecodedSubframe(decodedSubframeNumber);
    if (intermediateEphemeris.isFullyDecoded()) {
      partiallyDecodedIntermediateEphemerides[prn - 1] = null;
      fullyDecodedIntermediateEphemerides[prn - 1] = intermediateEphemeris;
    } else {
      partiallyDecodedIntermediateEphemerides[prn - 1] = intermediateEphemeris;
    }
  }

  /**
   * Extracts the requested bits from the raw stream.
   *
   * @param index Zero-based index of the first bit to extract.
   * @param length The length of the stream of bits to extract.
   * @param rawData The stream to extract data from.
   * @return The bits requested always shifted to the least significant positions.
   */
  private static int extractBits(int index, int length, byte[] rawData) {
    int result = 0;

    for (int i = 0; i < length; ++i) {
      int workingIndex = index + i;

      int wordIndex = workingIndex / WORD_SIZE_BITS;
      // account for 2 bit padding for every 30bit word
      workingIndex += (wordIndex + 1) * WORD_PADDING_BITS;
      int byteIndex = workingIndex / BYTE_AS_BITS;
      int byteOffset = workingIndex % BYTE_AS_BITS;

      byte raw = rawData[byteIndex];
      // account for zero-based indexing
      int shiftOffset = BYTE_AS_BITS - 1 - byteOffset;
      int mask = 1 << shiftOffset;
      int bit = raw & mask;
      bit >>= shiftOffset;

      // account for zero-based indexing
      result |= bit << length - 1 - i;
    }
    return result;
  }

  /**
   * Extracts an unsigned 32 bit word where the word is partitioned 8/24 bits.
   *
   * @param index8 The index of the first 8 bits used.
   * @param index24 The index of the last 24 bits used.
   * @param rawData The stream to extract data from.
   * @return The bits requested represented as a long and stored in the least significant positions.
   */
  private static long buildUnsigned32BitsWordFrom8And24Words(
      int index8, int index24, byte[] rawData) {
    long result = (long) extractBits(index8, 8, rawData) << 24;
    result |= extractBits(index24, 24, rawData);
    return result;
  }

  /**
   * Extracts a signed 32 bit word where the word is partitioned 8/24 bits with LSB first.
   *
   * @param index8 The index of the first 8 bits used.
   * @param index24 The index of the last 24 bits used.
   * @param rawData The stream to extract data from.
   * @return The bits requested represented as an int and stored in the least significant positions.
   */
  private static int buildSigned32BitsWordFrom8And24WordsWith8bitslsb(
      int index8, int index24, byte[] rawData) {
    int result = extractBits(index24, 24, rawData) << 8;
    result |= extractBits(index8, 8, rawData);
    return result;
  }

  /**
   * Calculates the 2s complement for a specific number of bits of a given value
   *
   * @param value The set of bits to translate.
   * @param bits The number of bits to consider.
   * @return The calculated 2s complement.
   */
  private static int getTwoComplement(int value, int bits) {
    int msbMask = 1 << bits - 1;
    int msb = value & msbMask;
    if (msb == 0) {
      // the value is positive
      return value;
    }

    int valueBitMask = (1 << bits) - 1;
    int extendedSignMask = (int) INTEGER_RANGE - valueBitMask;
    return value | extendedSignMask;
  }

  /**
   * Calculates the GPS week with rollovers. A rollover happens every 1024 weeks, beginning from GPS
   * epoch (January 6, 1980).
   *
   * @param gpsWeek The modulo-1024 GPS week.
   * @return The absolute GPS week.
   */
  private static int getGpsWeekWithRollover(int gpsWeek) {
    long nowMs = System.currentTimeMillis();
    long elapsedTimeFromGpsEpochMs = nowMs - GPS_EPOCH_AS_UNIX_EPOCH_MS;
    long rolloverCycles = elapsedTimeFromGpsEpochMs / GPS_CYCLE_MS;
    int rolloverWeeks = (int) rolloverCycles * GPS_CYCLE_WEEKS;
    return gpsWeek + rolloverWeeks;
  }

  /**
   * Computes a nominal Sv Accuracy based on the URA index. This implementation is taken from
   * http://www.gps.gov/technical/icwg/IS-GPS-200D.pdf, section '20.3.3.3.1.3 Sv Accuracy'.
   *
   * @param uraIndex The URA Index
   * @return A computed nominal Sv accuracy.
   */
  private static double computeNominalSvAccuracy(int uraIndex) {
    if (uraIndex < 0 || uraIndex >= 15) {
      return Double.NaN;
    } else if (uraIndex == 1) {
      return 2.8;
    } else if (uraIndex == 3) {
      return 5.7;
    } else if (uraIndex == 5) {
      return 11.3;
    }

    int exponent;
    if (uraIndex < 6) {
      exponent = 1 + (uraIndex / 2);
    } else {
      exponent = uraIndex - 2;
    }
    return Math.pow(2, exponent);
  }

  /**
   * Finds an {@link IntermediateEphemeris} that can be updated by the given data. The pseudocode is
   * as follows:
   *
   * <p>if a fully decoded message is available and matches, there is no need to update
   *
   * <p>if a partially decoded message is available and matches, there is no need to update
   *
   * <p>if the provided issueOfData matches intermediate partially decoded state, update in place
   *
   * <p>otherwise, start a new decoding 'session' for the prn
   *
   * @param prn The prn to update
   * @param subframe The subframe available to update
   * @param issueOfData The issueOfData associated with the given subframe
   * @return a {@link IntermediateEphemeris} to update with the available data, {@code null} if
   *     there is no need to update a {@link IntermediateEphemeris}.
   */
  private IntermediateEphemeris findIntermediateEphemerisToUpdate(
      byte prn, int subframe, int issueOfData) {
    // find out if we have fully decoded up-to-date ephemeris first
    IntermediateEphemeris fullyDecodedIntermediateEphemeris =
        this.fullyDecodedIntermediateEphemerides[prn - 1];
    if (fullyDecodedIntermediateEphemeris != null
        && fullyDecodedIntermediateEphemeris
            .findSubframeInfo(prn, subframe, issueOfData)
            .isSubframeDecoded()) {
      return null;
    }

    // find out next if there is a partially decoded intermediate state we can continue working on
    IntermediateEphemeris partiallyDecodedIntermediateEphemeris =
        this.partiallyDecodedIntermediateEphemerides[prn - 1];
    if (partiallyDecodedIntermediateEphemeris == null) {
      // no intermediate partially decoded state, we need to start a decoding 'session'
      return new IntermediateEphemeris(prn);
    }
    SubframeCheckResult subframeCheckResult =
        partiallyDecodedIntermediateEphemeris.findSubframeInfo(prn, subframe, issueOfData);
    if (subframeCheckResult.isSubframeDecoded()) {
      return null;
    }
    if (subframeCheckResult.hasSubframe && !subframeCheckResult.issueOfDataMatches) {
      // the navigation message has changed, we need to start over
      return new IntermediateEphemeris(prn);
    }

    int intermediateIode = Integer.MAX_VALUE;
    boolean intermediateHasIode = false;
    GpsEphemerisProto gpsEphemerisProto = partiallyDecodedIntermediateEphemeris.getEphemerisObj();

    if (partiallyDecodedIntermediateEphemeris.hasDecodedSubframe(SUBFRAME_1)) {
      intermediateHasIode = true;
      intermediateIode = gpsEphemerisProto.iodc & IODE_TO_IODC_MASK;
    }
    if (partiallyDecodedIntermediateEphemeris.hasDecodedSubframe(SUBFRAME_2)
        || partiallyDecodedIntermediateEphemeris.hasDecodedSubframe(SUBFRAME_3)) {
      intermediateHasIode = true;
      intermediateIode = gpsEphemerisProto.iode;
    }

    boolean canContinueDecoding;
    int iode;
    switch (subframe) {
      case SUBFRAME_1:
        iode = issueOfData & IODE_TO_IODC_MASK;
        canContinueDecoding = !intermediateHasIode || (intermediateIode == iode);
        break;
      case SUBFRAME_2:
        // fall through
      case SUBFRAME_3:
        iode = issueOfData;
        canContinueDecoding = !intermediateHasIode || (intermediateIode == iode);
        break;
      case SUBFRAME_4:
        // fall through
      case SUBFRAME_5:
        // always continue decoding for subframes 4-5
        canContinueDecoding = true;
        break;
      default:
        throw new IllegalStateException("invalid subframe requested: " + subframe);
    }

    if (canContinueDecoding) {
      return partiallyDecodedIntermediateEphemeris;
    }
    return new IntermediateEphemeris(prn);
  }

  /**
   * A representation of an intermediate ephemeris that can be fully decoded or partially decoded.
   */
  private static class IntermediateEphemeris {

    private final GpsEphemerisProto gpsEphemerisProtoObj = new GpsEphemerisProto();

    private int subframesDecoded;

    public IntermediateEphemeris(byte prn) {
      gpsEphemerisProtoObj.prn = prn;
    }

    public void reportDecodedSubframe(int subframe) {
      subframesDecoded |= subframe;
    }

    public boolean hasDecodedSubframe(int subframe) {
      return (subframesDecoded & subframe) == subframe;
    }

    public boolean isFullyDecoded() {
      return hasDecodedSubframe(SUBFRAME_1)
          && hasDecodedSubframe(SUBFRAME_2)
          && hasDecodedSubframe(SUBFRAME_3);
    }

    public GpsEphemerisProto getEphemerisObj() {
      return gpsEphemerisProtoObj;
    }

    /**
     * Verifies that the received subframe info (IODE and IODC) matches the existing info (IODE and
     * IODC). For each subframe there is a given issueOfData that must match, this method abstracts
     * the logic to perform such check.
     *
     * @param prn The expected prn.
     * @param subframe The expected subframe.
     * @param issueOfData The issueOfData for the given subframe.
     * @return {@link SubframeCheckResult} representing the state found.
     */
    public SubframeCheckResult findSubframeInfo(byte prn, int subframe, int issueOfData) {
      if (gpsEphemerisProtoObj.prn != prn) {
        return new SubframeCheckResult(false /* hasSubframe */, false /* issueOfDataMatches */);
      }
      boolean issueOfDataMatches;
      switch (subframe) {
        case SUBFRAME_1:
          issueOfDataMatches = gpsEphemerisProtoObj.iodc == issueOfData;
          break;
        case SUBFRAME_2:
          // fall through
        case SUBFRAME_3:
          issueOfDataMatches = gpsEphemerisProtoObj.iode == issueOfData;
          break;
        case SUBFRAME_4:
          // fall through
        case SUBFRAME_5:
          // subframes 4-5 do not have IOD to match, so we assume they always match
          issueOfDataMatches = true;
          break;
        default:
          throw new IllegalArgumentException("Invalid subframe provided: " + subframe);
      }
      boolean hasDecodedSubframe = hasDecodedSubframe(subframe);
      return new SubframeCheckResult(hasDecodedSubframe, issueOfDataMatches);
    }
  }

  /**
   * Represents a result while finding a subframe in an intermediate {@link IntermediateEphemeris}.
   */
  private static class SubframeCheckResult {

    /** The intermediate {@link IntermediateEphemeris} has the requested subframe. */
    public final boolean hasSubframe;

    /**
     * The issue of data, associated with the requested subframe, matches the subframe found in the
     * intermediate state.
     */
    public final boolean issueOfDataMatches;

    public SubframeCheckResult(boolean hasSubframe, boolean issueOfDataMatches) {
      this.hasSubframe = hasSubframe;
      this.issueOfDataMatches = issueOfDataMatches;
    }

    /**
     * @return {@code true} if the requested subframe has been decoded in the intermediate state,
     *     {@code false} otherwise.
     */
    public boolean isSubframeDecoded() {
      return hasSubframe && issueOfDataMatches;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/GpsTime.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import android.util.Pair;
import com.google.common.base.Preconditions;
import com.google.common.primitives.Longs;
import java.util.Calendar;
import java.util.concurrent.TimeUnit;
import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;

/** A simple class to represent time unit used by GPS. */
public class GpsTime implements Comparable<GpsTime> {
  public static final int MILLIS_IN_SECOND = 1000;
  public static final int SECONDS_IN_MINUTE = 60;
  public static final int MINUTES_IN_HOUR = 60;
  public static final int HOURS_IN_DAY = 24;
  public static final int SECONDS_IN_DAY = HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE;
  public static final int DAYS_IN_WEEK = 7;
  public static final long MILLIS_IN_DAY = TimeUnit.DAYS.toMillis(1);
  public static final long MILLIS_IN_WEEK = TimeUnit.DAYS.toMillis(7);
  public static final long NANOS_IN_WEEK = TimeUnit.DAYS.toNanos(7);
  // GPS epoch is 1980/01/06
  public static final long GPS_DAYS_SINCE_JAVA_EPOCH = 3657;
  public static final long GPS_UTC_EPOCH_OFFSET_SECONDS =
      TimeUnit.DAYS.toSeconds(GPS_DAYS_SINCE_JAVA_EPOCH);
  public static final long GPS_UTC_EPOCH_OFFSET_NANOS =
      TimeUnit.SECONDS.toNanos(GPS_UTC_EPOCH_OFFSET_SECONDS);
  private static final DateTimeZone UTC_ZONE = DateTimeZone.UTC;
  private static final DateTime LEAP_SECOND_DATE_1981 = new DateTime(1981, 7, 1, 0, 0, UTC_ZONE);
  private static final DateTime LEAP_SECOND_DATE_2012 = new DateTime(2012, 7, 1, 0, 0, UTC_ZONE);
  private static final DateTime LEAP_SECOND_DATE_2015 = new DateTime(2015, 7, 1, 0, 0, UTC_ZONE);
  private static final DateTime LEAP_SECOND_DATE_2017 = new DateTime(2017, 1, 1, 0, 0, UTC_ZONE);
  // nanoseconds since GPS epoch (1980/1/6).
  private long gpsNanos;

  /**
   * Constructor for GpsTime. Input values are all in GPS time.
   *
   * @param year Year
   * @param month Month from 1 to 12
   * @param day Day from 1 to 31
   * @param hour Hour from 0 to 23
   * @param minute Minute from 0 to 59
   * @param second Second from 0 to 59
   */
  public GpsTime(int year, int month, int day, int hour, int minute, double second) {
    DateTime utcDateTime =
        new DateTime(
            year, month, day, hour, minute, (int) second, (int) (second * 1000) % 1000, UTC_ZONE);

    // Since input time is already specify in GPS time, no need to count leap second here.
    gpsNanos = TimeUnit.MILLISECONDS.toNanos(utcDateTime.getMillis()) - GPS_UTC_EPOCH_OFFSET_NANOS;
  }

  /**
   * Constructor
   *
   * @param dateTime is created using GPS time values.
   */
  public GpsTime(DateTime dateTime) {
    gpsNanos = TimeUnit.MILLISECONDS.toNanos(dateTime.getMillis()) - GPS_UTC_EPOCH_OFFSET_NANOS;
  }

  /**
   * Constructor
   *
   * @param gpsNanos nanoseconds since GPS epoch.
   */
  public GpsTime(long gpsNanos) {
    this.gpsNanos = gpsNanos;
  }

  /**
   * Creates a GPS time using a UTC based date and time.
   *
   * @param dateTime represents the current time in UTC time, must be after 2009
   */
  public static GpsTime fromUtc(DateTime dateTime) {
    return new GpsTime(
        TimeUnit.MILLISECONDS.toNanos(dateTime.getMillis())
            + TimeUnit.SECONDS.toNanos(
                GpsTime.getLeapSecond(dateTime) - GPS_UTC_EPOCH_OFFSET_SECONDS));
  }

  /** Creates a GPS time based upon the current time. */
  public static GpsTime now() {
    return fromUtc(DateTime.now(DateTimeZone.UTC));
  }

  /**
   * Creates a GPS time using absolute GPS week number, and the time of week.
   *
   * @param gpsWeek
   * @param towSec GPS time of week in second
   * @return actual time in GpsTime.
   */
  public static GpsTime fromWeekTow(int gpsWeek, int towSec) {
    long nanos = gpsWeek * NANOS_IN_WEEK + TimeUnit.SECONDS.toNanos(towSec);
    return new GpsTime(nanos);
  }

  /**
   * Creates a GPS time using YUMA GPS week number (0..1023), and the time of week.
   *
   * @param yumaWeek (0..1023)
   * @param towSec GPS time of week in second
   * @return actual time in GpsTime.
   */
  public static GpsTime fromYumaWeekTow(int yumaWeek, int towSec) {
    Preconditions.checkArgument(yumaWeek >= 0);
    Preconditions.checkArgument(yumaWeek < 1024);

    // Estimate the multiplier of current week.
    DateTime currentTime = DateTime.now(UTC_ZONE);
    GpsTime refTime = new GpsTime(currentTime);
    Pair<Integer, Integer> refWeekSec = refTime.getGpsWeekSecond();
    int weekMultiplier = refWeekSec.first / 1024;

    int gpsWeek = weekMultiplier * 1024 + yumaWeek;
    return fromWeekTow(gpsWeek, towSec);
  }

  public static GpsTime fromTimeSinceGpsEpoch(long gpsSec) {
    return new GpsTime(TimeUnit.SECONDS.toNanos(gpsSec));
  }

  /**
   * Computes leap seconds. Only accurate after 2009.
   *
   * @param time
   * @return number of leap seconds since GPS epoch.
   */
  public static int getLeapSecond(DateTime time) {
    if (LEAP_SECOND_DATE_2017.compareTo(time) <= 0) {
      return 18;
    } else if (LEAP_SECOND_DATE_2015.compareTo(time) <= 0) {
      return 17;
    } else if (LEAP_SECOND_DATE_2012.compareTo(time) <= 0) {
      return 16;
    } else if (LEAP_SECOND_DATE_1981.compareTo(time) <= 0) {
      // Only correct between 2012/7/1 to 2008/12/31
      return 15;
    } else {
      return 0;
    }
  }

  /**
   * Computes GPS weekly epoch of the reference time.
   *
   * <p>GPS weekly epoch are defined as of every Sunday 00:00:000 (mor
   *
   * @param refTime reference time
   * @return nanoseconds since GPS epoch, for the week epoch.
   */
  public static Long getGpsWeekEpochNano(GpsTime refTime) {
    Pair<Integer, Integer> weekSecond = refTime.getGpsWeekSecond();
    return weekSecond.first * NANOS_IN_WEEK;
  }

  /** @return week count since GPS epoch, and second count since the beginning of that week. */
  public Pair<Integer, Integer> getGpsWeekSecond() {
    // JAVA/UNIX epoch: January 1, 1970 in msec
    // GPS epoch: January 6, 1980 in second
    int week = (int) (gpsNanos / NANOS_IN_WEEK);
    int second = (int) TimeUnit.NANOSECONDS.toSeconds(gpsNanos % NANOS_IN_WEEK);
    return Pair.create(week, second);
  }

  /**
   * @return week count since GPS epoch, and second count in 0.08 sec resolution, 23-bit
   *     presentation (required by RRLP.)"
   */
  public Pair<Integer, Integer> getGpsWeekTow23b() {
    // UNIX epoch: January 1, 1970 in msec
    // GPS epoch: January 6, 1980 in second
    int week = (int) (gpsNanos / NANOS_IN_WEEK);
    // 80 millis is 0.08 second.
    int tow23b = (int) TimeUnit.NANOSECONDS.toMillis(gpsNanos % NANOS_IN_WEEK) / 80;
    return Pair.create(week, tow23b);
  }

  public long[] getBreakdownEpoch(TimeUnit... units) {
    long nanos = this.gpsNanos;
    long[] values = new long[units.length];
    for (int idx = 0; idx < units.length; ++idx) {
      TimeUnit unit = units[idx];
      long value = unit.convert(nanos, TimeUnit.NANOSECONDS);
      values[idx] = value;
      nanos -= unit.toNanos(value);
    }
    return values;
  }

  /** @return Day of year in GPS time (GMT time) */
  public static int getCurrentDayOfYear() {
    DateTime current = DateTime.now(DateTimeZone.UTC);
    // Since current is derived from UTC time, we need to add leap second here.
    long gpsTimeMillis = current.getMillis() + getLeapSecond(current);
    DateTime gpsCurrent = new DateTime(gpsTimeMillis, UTC_ZONE);
    return gpsCurrent.getDayOfYear();
  }

  /** @return milliseconds since JAVA/UNIX epoch. */
  public final long getMillisSinceJavaEpoch() {
    return TimeUnit.NANOSECONDS.toMillis(gpsNanos + GPS_UTC_EPOCH_OFFSET_NANOS);
  }

  /** @return milliseconds since GPS epoch. */
  public final long getMillisSinceGpsEpoch() {
    return TimeUnit.NANOSECONDS.toMillis(gpsNanos);
  }

  /** @return microseconds since GPS epoch. */
  public final long getMicrosSinceGpsEpoch() {
    return TimeUnit.NANOSECONDS.toMicros(gpsNanos);
  }

  /** @return nanoseconds since GPS epoch. */
  public final long getNanosSinceGpsEpoch() {
    return gpsNanos;
  }

  /** @return the GPS time in Calendar. */
  public Calendar getTimeInCalendar() {
    return getGpsDateTime().toGregorianCalendar();
  }

  /** @return a DateTime with leap seconds considered. */
  public DateTime getUtcDateTime() {
    DateTime gpsDateTime = getGpsDateTime();
    return new DateTime(
        gpsDateTime.getMillis() - TimeUnit.SECONDS.toMillis(getLeapSecond(gpsDateTime)), UTC_ZONE);
  }

  /** @return a DateTime based on the pure GPS time (without considering leap second). */
  public DateTime getGpsDateTime() {
    return new DateTime(
        TimeUnit.NANOSECONDS.toMillis(gpsNanos + GPS_UTC_EPOCH_OFFSET_NANOS), UTC_ZONE);
  }

  /**
   * Compares two {@code GpsTime} objects temporally.
   *
   * @param other the {@code GpsTime} to be compared.
   * @return the value {@code 0} if this {@code GpsTime} is simultaneous with the argument {@code
   *     GpsTime}; a value less than {@code 0} if this {@code GpsTime} occurs before the argument
   *     {@code GpsTime}; and a value greater than {@code 0} if this {@code GpsTime} occurs after
   *     the argument {@code GpsTime} (signed comparison).
   */
  @Override
  public int compareTo(GpsTime other) {
    return Long.compare(this.getNanosSinceGpsEpoch(), other.getNanosSinceGpsEpoch());
  }

  @Override
  public boolean equals(Object other) {
    if (!(other instanceof GpsTime)) {
      return false;
    }
    GpsTime time = (GpsTime) other;
    return getNanosSinceGpsEpoch() == time.getNanosSinceGpsEpoch();
  }

  @Override
  public int hashCode() {
    return Longs.hashCode(getNanosSinceGpsEpoch());
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/IonosphericModel.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import com.google.location.lbs.gnss.gps.pseudorange.Ecef2LlaConverter.GeodeticLlaValues;
import com.google.location.lbs.gnss.gps.pseudorange.EcefToTopocentricConverter.TopocentricAEDValues;

/**
 * Calculates the Ionospheric correction of the pseudorange given the {@code userPosition}, {@code
 * satellitePosition}, {@code gpsTimeSeconds} and the ionospheric parameters sent by the satellite
 * {@code alpha} and {@code beta}
 *
 * <p>Source: http://www.navipedia.net/index.php/Klobuchar_Ionospheric_Model and
 * http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4104345 and
 * http://www.ion.org/museum/files/ACF2A4.pdf
 */
public class IonosphericModel {
  /** Center frequency of the L1 band in Hz. */
  public static final double L1_FREQ_HZ = 10.23 * 1e6 * 154;
  /** Center frequency of the L2 band in Hz. */
  public static final double L2_FREQ_HZ = 10.23 * 1e6 * 120;
  /** Center frequency of the L5 band in Hz. */
  public static final double L5_FREQ_HZ = 10.23 * 1e6 * 115;

  private static final double SECONDS_PER_DAY = 86400.0;
  private static final double PERIOD_OF_DELAY_THRESHOLD_SECONDS = 72000.0;
  private static final double IPP_LATITUDE_THRESHOLD_SEMI_CIRCLE = 0.416;
  private static final double DC_TERM = 5.0e-9;
  private static final double NORTH_GEOMAGNETIC_POLE_LONGITUDE_RADIANS = 5.08;
  private static final double GEOMETRIC_LATITUDE_CONSTANT = 0.064;
  private static final int DELAY_PHASE_TIME_CONSTANT_SECONDS = 50400;
  private static final int IONO_0_IDX = 0;
  private static final int IONO_1_IDX = 1;
  private static final int IONO_2_IDX = 2;
  private static final int IONO_3_IDX = 3;

  /**
   * Calculates the Ionospheric correction of the pseudorange in seconds using the Klobuchar
   * Ionospheric model.
   */
  public static double ionoKlobucharCorrectionSeconds(
      double[] userPositionECEFMeters,
      double[] satellitePositionECEFMeters,
      double gpsTOWSeconds,
      double[] alpha,
      double[] beta,
      double frequencyHz) {

    TopocentricAEDValues elevationAndAzimuthRadians =
        EcefToTopocentricConverter.calculateElAzDistBetween2Points(
            userPositionECEFMeters, satellitePositionECEFMeters);
    double elevationSemiCircle = elevationAndAzimuthRadians.elevationRadians / Math.PI;
    double azimuthSemiCircle = elevationAndAzimuthRadians.azimuthRadians / Math.PI;
    GeodeticLlaValues latLngAlt =
        Ecef2LlaConverter.convertECEFToLLACloseForm(
            userPositionECEFMeters[0], userPositionECEFMeters[1], userPositionECEFMeters[2]);
    double latitudeUSemiCircle = latLngAlt.latitudeRadians / Math.PI;
    double longitudeUSemiCircle = latLngAlt.longitudeRadians / Math.PI;

    // earth's centered angle (semi-circles)
    double earthCentredAngleSemiCircle = 0.0137 / (elevationSemiCircle + 0.11) - 0.022;

    // latitude of the Ionospheric Pierce Point (IPP) (semi-circles)
    double latitudeISemiCircle =
        latitudeUSemiCircle + earthCentredAngleSemiCircle * Math.cos(azimuthSemiCircle * Math.PI);

    if (latitudeISemiCircle > IPP_LATITUDE_THRESHOLD_SEMI_CIRCLE) {
      latitudeISemiCircle = IPP_LATITUDE_THRESHOLD_SEMI_CIRCLE;
    } else if (latitudeISemiCircle < -IPP_LATITUDE_THRESHOLD_SEMI_CIRCLE) {
      latitudeISemiCircle = -IPP_LATITUDE_THRESHOLD_SEMI_CIRCLE;
    }

    // geodetic longitude of the Ionospheric Pierce Point (IPP) (semi-circles)
    double longitudeISemiCircle =
        longitudeUSemiCircle
            + earthCentredAngleSemiCircle
                * Math.sin(azimuthSemiCircle * Math.PI)
                / Math.cos(latitudeISemiCircle * Math.PI);

    // geomagnetic latitude of the Ionospheric Pierce Point (IPP) (semi-circles)
    double geomLatIPPSemiCircle =
        latitudeISemiCircle
            + GEOMETRIC_LATITUDE_CONSTANT
                * Math.cos(
                    longitudeISemiCircle * Math.PI - NORTH_GEOMAGNETIC_POLE_LONGITUDE_RADIANS);

    // local time (sec) at the Ionospheric Pierce Point (IPP)
    double localTimeSeconds = SECONDS_PER_DAY / 2.0 * longitudeISemiCircle + gpsTOWSeconds;
    localTimeSeconds %= SECONDS_PER_DAY;
    if (localTimeSeconds < 0) {
      localTimeSeconds += SECONDS_PER_DAY;
    }

    // amplitude of the ionospheric delay (seconds)
    double amplitudeOfDelaySeconds =
        alpha[IONO_0_IDX]
            + alpha[IONO_1_IDX] * geomLatIPPSemiCircle
            + alpha[IONO_2_IDX] * geomLatIPPSemiCircle * geomLatIPPSemiCircle
            + alpha[IONO_3_IDX]
                * geomLatIPPSemiCircle
                * geomLatIPPSemiCircle
                * geomLatIPPSemiCircle;
    if (amplitudeOfDelaySeconds < 0) {
      amplitudeOfDelaySeconds = 0;
    }

    // period of ionospheric delay
    double periodOfDelaySeconds =
        beta[IONO_0_IDX]
            + beta[IONO_1_IDX] * geomLatIPPSemiCircle
            + beta[IONO_2_IDX] * geomLatIPPSemiCircle * geomLatIPPSemiCircle
            + beta[IONO_3_IDX] * geomLatIPPSemiCircle * geomLatIPPSemiCircle * geomLatIPPSemiCircle;
    if (periodOfDelaySeconds < PERIOD_OF_DELAY_THRESHOLD_SECONDS) {
      periodOfDelaySeconds = PERIOD_OF_DELAY_THRESHOLD_SECONDS;
    }

    // phase of ionospheric delay
    double phaseOfDelayRadians =
        2 * Math.PI * (localTimeSeconds - DELAY_PHASE_TIME_CONSTANT_SECONDS) / periodOfDelaySeconds;

    // slant factor
    double slantFactor = 1.0 + 16.0 * Math.pow(0.53 - elevationSemiCircle, 3);

    // ionospheric time delay (seconds)
    double ionoDelaySeconds;

    if (Math.abs(phaseOfDelayRadians) >= Math.PI / 2.0) {
      ionoDelaySeconds = DC_TERM * slantFactor;
    } else {
      ionoDelaySeconds =
          (DC_TERM
                  + (1
                          - Math.pow(phaseOfDelayRadians, 2) / 2.0
                          + Math.pow(phaseOfDelayRadians, 4) / 24.0)
                      * amplitudeOfDelaySeconds)
              * slantFactor;
    }

    // apply factor for frequency bands other than L1
    ionoDelaySeconds *= (L1_FREQ_HZ * L1_FREQ_HZ) / (frequencyHz * frequencyHz);

    return ionoDelaySeconds;
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/Lla2EcefConverter.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import com.google.location.lbs.gnss.gps.pseudorange.Ecef2LlaConverter.GeodeticLlaValues;

/**
 * A tool to convert geodetic latitude, longitude and altitude above planetary ellipsoid to
 * Earth-centered Earth-fixed (ECEF) Cartesian coordinates
 *
 * <p>Source: https://www.mathworks.com/help/aeroblks/llatoecefposition.html
 */
public class Lla2EcefConverter {
  private static final double ECCENTRICITY = 8.1819190842622e-2;
  private static final double EARTH_SEMI_MAJOR_AXIS_METERS = 6378137.0;

  /**
   * Converts LLA (latitude,longitude, and altitude) coordinates to ECEF (Earth-Centered
   * Earth-Fixed) Cartesian coordinates
   *
   * <p>Inputs is GeodeticLlaValues class {@link GeodeticLlaValues} containing geodetic latitude
   * (radians), geodetic longitude (radians), height above WGS84 ellipsoid (m)
   *
   * <p>Output is cartesian coordinates x,y,z in meters
   */
  public static double[] convertFromLlaToEcefMeters(GeodeticLlaValues llaValues) {
    double cosLatitude = Math.cos(llaValues.latitudeRadians);
    double cosLongitude = Math.cos(llaValues.longitudeRadians);
    double sinLatitude = Math.sin(llaValues.latitudeRadians);
    double sinLongitude = Math.sin(llaValues.longitudeRadians);

    double r0 =
        EARTH_SEMI_MAJOR_AXIS_METERS
            / Math.sqrt(1.0 - Math.pow(ECCENTRICITY, 2) * sinLatitude * sinLatitude);

    double[] positionEcefMeters = new double[3];
    positionEcefMeters[0] = (llaValues.altitudeMeters + r0) * cosLatitude * cosLongitude;
    positionEcefMeters[1] = (llaValues.altitudeMeters + r0) * cosLatitude * sinLongitude;
    positionEcefMeters[2] =
        (llaValues.altitudeMeters + r0 * (1.0 - Math.pow(ECCENTRICITY, 2))) * sinLatitude;
    return positionEcefMeters;
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/PseudorangeNoSmoothingSmoother.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import java.util.Collections;
import java.util.List;

/**
 * An implementation of {@link PseudorangeSmoother} that performs no smoothing.
 *
 * <p>A new list of {@link GpsMeasurementWithRangeAndUncertainty} instances is filled with a copy of
 * the input list.
 */
class PseudorangeNoSmoothingSmoother implements PseudorangeSmoother {

  @Override
  public List<GpsMeasurementWithRangeAndUncertainty> updatePseudorangeSmoothingResult(
      List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToGPSReceiverMeasurements) {
    return Collections.unmodifiableList(usefulSatellitesToGPSReceiverMeasurements);
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/PseudorangePositionVelocityFromRealTimeEvents.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import android.location.GnssClock;
import android.location.GnssMeasurement;
import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.cts.nano.Ephemeris.GpsEphemerisProto;
import android.location.cts.nano.Ephemeris.GpsNavMessageProto;
import android.location.cts.suplClient.SuplRrlpController;
import android.util.Log;
import com.google.location.lbs.gnss.gps.pseudorange.Ecef2EnuConverter.EnuValues;
import com.google.location.lbs.gnss.gps.pseudorange.Ecef2LlaConverter.GeodeticLlaValues;
import java.io.BufferedReader;
import java.io.IOException;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.List;
import java.util.concurrent.TimeUnit;

/**
 * Helper class for calculating Gps position and velocity solution using weighted least squares
 * where the raw Gps measurements are parsed as a {@link BufferedReader} with the option to apply
 * doppler smoothing, carrier phase smoothing or no smoothing.
 */
public class PseudorangePositionVelocityFromRealTimeEvents {

  private static final String TAG = "PseudorangePositionVelocityFromRealTimeEvents";
  private static final double SECONDS_PER_NANO = 1.0e-9;
  private static final int TOW_DECODED_MEASUREMENT_STATE_BIT = 3;
  /** Average signal travel time from GPS satellite and earth */
  private static final int MINIMUM_NUMBER_OF_USEFUL_SATELLITES = 4;

  private static final int C_TO_N0_THRESHOLD_DB_HZ = 18;

  private static final String SUPL_SERVER_NAME = "supl.google.com";
  private static final int SUPL_SERVER_PORT = 7276;

  private GpsNavMessageProto mHardwareGpsNavMessageProto = null;

  // navigation message parser
  private GpsNavigationMessageStore mGpsNavigationMessageStore = new GpsNavigationMessageStore();
  private double[] mPositionSolutionLatLngDeg = GpsMathOperations.createAndFillArray(3, Double.NaN);
  private double[] mVelocitySolutionEnuMps = GpsMathOperations.createAndFillArray(3, Double.NaN);
  private final double[] mPositionVelocityUncertaintyEnu =
      GpsMathOperations.createAndFillArray(6, Double.NaN);
  private double[] mPseudorangeResidualsMeters =
      GpsMathOperations.createAndFillArray(
          GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES, Double.NaN);
  private boolean mFirstUsefulMeasurementSet = true;
  private int[] mReferenceLocation = null;
  private long mLastReceivedSuplMessageTimeMillis = 0;
  private long mDeltaTimeMillisToMakeSuplRequest = TimeUnit.MINUTES.toMillis(30);
  private boolean mFirstSuplRequestNeeded = true;
  private GpsNavMessageProto mGpsNavMessageProtoUsed = null;

  // Only the interface of pseudorange smoother is provided. Please implement customized smoother.
  PseudorangeSmoother mPseudorangeSmoother = new PseudorangeNoSmoothingSmoother();
  private final UserPositionVelocityWeightedLeastSquare mUserPositionVelocityLeastSquareCalculator =
      new UserPositionVelocityWeightedLeastSquare(mPseudorangeSmoother);
  private GpsMeasurement[] mUsefulSatellitesToReceiverMeasurements =
      new GpsMeasurement[GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES];
  private Long[] mUsefulSatellitesToTowNs =
      new Long[GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES];
  private long mLargestTowNs = Long.MIN_VALUE;
  private double mArrivalTimeSinceGPSWeekNs = 0.0;
  private int mDayOfYear1To366 = 0;
  private int mGpsWeekNumber = 0;
  private long mArrivalTimeSinceGpsEpochNs = 0;

  /**
   * Computes Weighted least square position and velocity solutions from a received {@link
   * GnssMeasurementsEvent} and store the result in {@link
   * PseudorangePositionVelocityFromRealTimeEvents#mPositionSolutionLatLngDeg} and {@link
   * PseudorangePositionVelocityFromRealTimeEvents#mVelocitySolutionEnuMps}
   */
  public void computePositionVelocitySolutionsFromRawMeas(GnssMeasurementsEvent event)
      throws Exception {
    if (mReferenceLocation == null) {
      // If no reference location is received, we can not get navigation message from SUPL and hence
      // we will not try to compute location.
      Log.d(TAG, " No reference Location ..... no position is calculated");
      return;
    }
    for (int i = 0; i < GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES; i++) {
      mUsefulSatellitesToReceiverMeasurements[i] = null;
      mUsefulSatellitesToTowNs[i] = null;
    }

    GnssClock gnssClock = event.getClock();
    mArrivalTimeSinceGpsEpochNs = gnssClock.getTimeNanos() - gnssClock.getFullBiasNanos();

    for (GnssMeasurement measurement : event.getMeasurements()) {
      // ignore any measurement if it is not from GPS constellation
      if (measurement.getConstellationType() != GnssStatus.CONSTELLATION_GPS) {
        continue;
      }
      // ignore raw data if time is zero, if signal to noise ratio is below threshold or if
      // TOW is not yet decoded
      if (measurement.getCn0DbHz() >= C_TO_N0_THRESHOLD_DB_HZ
          && (measurement.getState() & (1L << TOW_DECODED_MEASUREMENT_STATE_BIT)) != 0) {

        // calculate day of year and Gps week number needed for the least square
        GpsTime gpsTime = new GpsTime(mArrivalTimeSinceGpsEpochNs);
        // Gps weekly epoch in Nanoseconds: defined as of every Sunday night at 00:00:000
        long gpsWeekEpochNs = GpsTime.getGpsWeekEpochNano(gpsTime);
        mArrivalTimeSinceGPSWeekNs = mArrivalTimeSinceGpsEpochNs - gpsWeekEpochNs;
        mGpsWeekNumber = gpsTime.getGpsWeekSecond().first;
        // calculate day of the year between 1 and 366
        Calendar cal = gpsTime.getTimeInCalendar();
        mDayOfYear1To366 = cal.get(Calendar.DAY_OF_YEAR);

        long receivedGPSTowNs = measurement.getReceivedSvTimeNanos();
        if (receivedGPSTowNs > mLargestTowNs) {
          mLargestTowNs = receivedGPSTowNs;
        }
        mUsefulSatellitesToTowNs[measurement.getSvid() - 1] = receivedGPSTowNs;
        GpsMeasurement gpsReceiverMeasurement =
            new GpsMeasurement(
                (long) mArrivalTimeSinceGPSWeekNs,
                measurement.getAccumulatedDeltaRangeMeters(),
                isAccumulatedDeltaRangeStateValid(measurement.getAccumulatedDeltaRangeState()),
                measurement.getPseudorangeRateMetersPerSecond(),
                measurement.getCn0DbHz(),
                measurement.getAccumulatedDeltaRangeUncertaintyMeters(),
                measurement.getPseudorangeRateUncertaintyMetersPerSecond());
        mUsefulSatellitesToReceiverMeasurements[measurement.getSvid() - 1] = gpsReceiverMeasurement;
      }
    }

    // check if we should continue using the navigation message from the SUPL server, or use the
    // navigation message from the device if we fully received it
    boolean useNavMessageFromSupl =
        continueUsingNavMessageFromSupl(
            mUsefulSatellitesToReceiverMeasurements, mHardwareGpsNavMessageProto);
    if (useNavMessageFromSupl) {
      Log.d(TAG, "Using navigation message from SUPL server");

      if (mFirstSuplRequestNeeded
          || (System.currentTimeMillis() - mLastReceivedSuplMessageTimeMillis)
              > mDeltaTimeMillisToMakeSuplRequest) {
        // The following line is blocking call for SUPL connection and back. But it is fast enough
        mGpsNavMessageProtoUsed = getSuplNavMessage(mReferenceLocation[0], mReferenceLocation[1]);
        if (!isEmptyNavMessage(mGpsNavMessageProtoUsed)) {
          mFirstSuplRequestNeeded = false;
          mLastReceivedSuplMessageTimeMillis = System.currentTimeMillis();
        } else {
          return;
        }
      }

    } else {
      Log.d(TAG, "Using navigation message from the GPS receiver");
      mGpsNavMessageProtoUsed = mHardwareGpsNavMessageProto;
    }

    // some times the SUPL server returns less satellites than the visible ones, so remove those
    // visible satellites that are not returned by SUPL
    for (int i = 0; i < GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES; i++) {
      if (mUsefulSatellitesToReceiverMeasurements[i] != null
          && !navMessageProtoContainsSvid(mGpsNavMessageProtoUsed, i + 1)) {
        mUsefulSatellitesToReceiverMeasurements[i] = null;
        mUsefulSatellitesToTowNs[i] = null;
      }
    }

    // calculate the number of useful satellites
    int numberOfUsefulSatellites = 0;
    for (GpsMeasurement element : mUsefulSatellitesToReceiverMeasurements) {
      if (element != null) {
        numberOfUsefulSatellites++;
      }
    }
    if (numberOfUsefulSatellites >= MINIMUM_NUMBER_OF_USEFUL_SATELLITES) {
      // ignore first set of > 4 satellites as they often result in erroneous position
      if (!mFirstUsefulMeasurementSet) {
        // start with last known position and velocity of zero. Following the structure:
        // [X position, Y position, Z position, clock bias,
        //  X Velocity, Y Velocity, Z Velocity, clock bias rate]
        double[] positionVelocitySolutionEcef = GpsMathOperations.createAndFillArray(8, 0);
        double[] positionVelocityUncertaintyEnu = GpsMathOperations.createAndFillArray(6, 0);
        double[] pseudorangeResidualMeters =
            GpsMathOperations.createAndFillArray(
                GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES, Double.NaN);
        performPositionVelocityComputationEcef(
            mUserPositionVelocityLeastSquareCalculator,
            mUsefulSatellitesToReceiverMeasurements,
            mUsefulSatellitesToTowNs,
            mLargestTowNs,
            mArrivalTimeSinceGPSWeekNs,
            mDayOfYear1To366,
            mGpsWeekNumber,
            positionVelocitySolutionEcef,
            positionVelocityUncertaintyEnu,
            pseudorangeResidualMeters);
        // convert the position solution from ECEF to latitude, longitude and altitude
        GeodeticLlaValues latLngAlt =
            Ecef2LlaConverter.convertECEFToLLACloseForm(
                positionVelocitySolutionEcef[0],
                positionVelocitySolutionEcef[1],
                positionVelocitySolutionEcef[2]);
        mPositionSolutionLatLngDeg[0] = Math.toDegrees(latLngAlt.latitudeRadians);
        mPositionSolutionLatLngDeg[1] = Math.toDegrees(latLngAlt.longitudeRadians);
        mPositionSolutionLatLngDeg[2] = latLngAlt.altitudeMeters;
        mPositionVelocityUncertaintyEnu[0] = positionVelocityUncertaintyEnu[0];
        mPositionVelocityUncertaintyEnu[1] = positionVelocityUncertaintyEnu[1];
        mPositionVelocityUncertaintyEnu[2] = positionVelocityUncertaintyEnu[2];
        System.arraycopy(
            pseudorangeResidualMeters,
            0 /*source starting pos*/,
            mPseudorangeResidualsMeters,
            0 /*destination starting pos*/,
            GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES /*length of elements*/);
        Log.d(
            TAG,
            "Position Uncertainty ENU Meters :"
                + mPositionVelocityUncertaintyEnu[0]
                + " "
                + mPositionVelocityUncertaintyEnu[1]
                + " "
                + mPositionVelocityUncertaintyEnu[2]);
        Log.d(
            TAG,
            "Latitude, Longitude, Altitude: "
                + mPositionSolutionLatLngDeg[0]
                + " "
                + mPositionSolutionLatLngDeg[1]
                + " "
                + mPositionSolutionLatLngDeg[2]);
        EnuValues velocityEnu =
            Ecef2EnuConverter.convertEcefToEnu(
                positionVelocitySolutionEcef[4],
                positionVelocitySolutionEcef[5],
                positionVelocitySolutionEcef[6],
                latLngAlt.latitudeRadians,
                latLngAlt.longitudeRadians);

        mVelocitySolutionEnuMps[0] = velocityEnu.enuEast;
        mVelocitySolutionEnuMps[1] = velocityEnu.enuNorth;
        mVelocitySolutionEnuMps[2] = velocityEnu.enuUP;
        Log.d(
            TAG,
            "Velocity ENU Mps: "
                + mVelocitySolutionEnuMps[0]
                + " "
                + mVelocitySolutionEnuMps[1]
                + " "
                + mVelocitySolutionEnuMps[2]);
        mPositionVelocityUncertaintyEnu[3] = positionVelocityUncertaintyEnu[3];
        mPositionVelocityUncertaintyEnu[4] = positionVelocityUncertaintyEnu[4];
        mPositionVelocityUncertaintyEnu[5] = positionVelocityUncertaintyEnu[5];
        Log.d(
            TAG,
            "Velocity Uncertainty ENU Mps :"
                + mPositionVelocityUncertaintyEnu[3]
                + " "
                + mPositionVelocityUncertaintyEnu[4]
                + " "
                + mPositionVelocityUncertaintyEnu[5]);
      }
      mFirstUsefulMeasurementSet = false;
    } else {
      Log.d(
          TAG,
          "Less than four satellites with SNR above threshold visible ... "
              + "no position is calculated!");

      mPositionSolutionLatLngDeg = GpsMathOperations.createAndFillArray(3, Double.NaN);
      mVelocitySolutionEnuMps = GpsMathOperations.createAndFillArray(3, Double.NaN);
      mPseudorangeResidualsMeters =
          GpsMathOperations.createAndFillArray(
              GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES, Double.NaN);
    }
  }

  private boolean isEmptyNavMessage(GpsNavMessageProto navMessageProto) {
    if (navMessageProto.iono == null) return true;
    if (navMessageProto.ephemerids.length == 0) return true;
    return false;
  }

  private boolean navMessageProtoContainsSvid(GpsNavMessageProto navMessageProto, int svid) {
    List<GpsEphemerisProto> ephemeridesList =
        new ArrayList<GpsEphemerisProto>(Arrays.asList(navMessageProto.ephemerids));
    for (GpsEphemerisProto ephProtoFromList : ephemeridesList) {
      if (ephProtoFromList.prn == svid) {
        return true;
      }
    }
    return false;
  }

  /**
   * Calculates ECEF least square position and velocity solutions from an array of {@link
   * GpsMeasurement} in meters and meters per second and store the result in {@code
   * positionVelocitySolutionEcef}
   */
  private void performPositionVelocityComputationEcef(
      UserPositionVelocityWeightedLeastSquare userPositionVelocityLeastSquare,
      GpsMeasurement[] usefulSatellitesToReceiverMeasurements,
      Long[] usefulSatellitesToTOWNs,
      long largestTowNs,
      double arrivalTimeSinceGPSWeekNs,
      int dayOfYear1To366,
      int gpsWeekNumber,
      double[] positionVelocitySolutionEcef,
      double[] positionVelocityUncertaintyEnu,
      double[] pseudorangeResidualMeters)
      throws Exception {

    List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToPseudorangeMeasurements =
        UserPositionVelocityWeightedLeastSquare.computePseudorangeAndUncertainties(
            Arrays.asList(usefulSatellitesToReceiverMeasurements),
            usefulSatellitesToTOWNs,
            largestTowNs);

    // calculate iterative least square position solution and velocity solutions
    userPositionVelocityLeastSquare.calculateUserPositionVelocityLeastSquare(
        mGpsNavMessageProtoUsed,
        usefulSatellitesToPseudorangeMeasurements,
        arrivalTimeSinceGPSWeekNs * SECONDS_PER_NANO,
        gpsWeekNumber,
        dayOfYear1To366,
        positionVelocitySolutionEcef,
        positionVelocityUncertaintyEnu,
        pseudorangeResidualMeters);

    Log.d(
        TAG,
        "Least Square Position Solution in ECEF meters: "
            + positionVelocitySolutionEcef[0]
            + " "
            + positionVelocitySolutionEcef[1]
            + " "
            + positionVelocitySolutionEcef[2]);
    Log.d(TAG, "Estimated Receiver clock offset in meters: " + positionVelocitySolutionEcef[3]);

    Log.d(
        TAG,
        "Velocity Solution in ECEF Mps: "
            + positionVelocitySolutionEcef[4]
            + " "
            + positionVelocitySolutionEcef[5]
            + " "
            + positionVelocitySolutionEcef[6]);
    Log.d(TAG, "Estimated Receiver clock offset rate in mps: " + positionVelocitySolutionEcef[7]);
  }

  /**
   * Reads the navigation message from the SUPL server by creating a Stubby client to Stubby server
   * that wraps the SUPL server. The input is the time in nanoseconds since the GPS epoch at which
   * the navigation message is required and the output is a {@link GpsNavMessageProto}
   *
   * @throws IOException
   * @throws UnknownHostException
   */
  private GpsNavMessageProto getSuplNavMessage(long latE7, long lngE7)
      throws UnknownHostException, IOException {
    SuplRrlpController suplRrlpController =
        new SuplRrlpController(SUPL_SERVER_NAME, SUPL_SERVER_PORT);
    GpsNavMessageProto navMessageProto = suplRrlpController.generateNavMessage(latE7, lngE7);

    return navMessageProto;
  }

  /**
   * Checks if we should continue using the navigation message from the SUPL server, or use the
   * navigation message from the device if we fully received it. If the navigation message read from
   * the receiver has all the visible satellite ephemerides, return false, otherwise, return true.
   */
  private static boolean continueUsingNavMessageFromSupl(
      GpsMeasurement[] usefulSatellitesToReceiverMeasurements,
      GpsNavMessageProto hardwareGpsNavMessageProto) {
    boolean useNavMessageFromSupl = true;
    if (hardwareGpsNavMessageProto != null) {
      ArrayList<GpsEphemerisProto> hardwareEphemeridesList =
          new ArrayList<GpsEphemerisProto>(Arrays.asList(hardwareGpsNavMessageProto.ephemerids));
      if (hardwareGpsNavMessageProto.iono != null) {
        for (int i = 0; i < GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES; i++) {
          if (usefulSatellitesToReceiverMeasurements[i] != null) {
            int prn = i + 1;
            for (GpsEphemerisProto hardwareEphProtoFromList : hardwareEphemeridesList) {
              if (hardwareEphProtoFromList.prn == prn) {
                useNavMessageFromSupl = false;
                break;
              }
              useNavMessageFromSupl = true;
            }
            if (useNavMessageFromSupl == true) {
              break;
            }
          }
        }
      }
    }
    return useNavMessageFromSupl;
  }

  /**
   * Returns the result of the GnssMeasurement.ADR_STATE_VALID bitmask being applied to the
   * AccumulatedDeltaRangeState from a GnssMeasurement - true if the ADR state is valid, false if it
   * is not
   *
   * @param accumulatedDeltaRangeState accumulatedDeltaRangeState from GnssMeasurement
   * @return the result of the GnssMeasurement.ADR_STATE_VALID bitmask being applied to the *
   *     AccumulatedDeltaRangeState of the given GnssMeasurement - true if the ADR state is valid, *
   *     false if it is not
   */
  private static boolean isAccumulatedDeltaRangeStateValid(int accumulatedDeltaRangeState) {
    return (GnssMeasurement.ADR_STATE_VALID & accumulatedDeltaRangeState)
        == GnssMeasurement.ADR_STATE_VALID;
  }

  /**
   * Parses a string array containing an updates to the navigation message and return the most
   * recent {@link GpsNavMessageProto}.
   */
  public void parseHwNavigationMessageUpdates(GnssNavigationMessage navigationMessage) {
    byte messagePrn = (byte) navigationMessage.getSvid();
    byte messageType = (byte) (navigationMessage.getType() >> 8);
    int subMessageId = navigationMessage.getSubmessageId();

    byte[] messageRawData = navigationMessage.getData();
    // parse only GPS navigation messages for now
    if (messageType == 1) {
      mGpsNavigationMessageStore.onNavMessageReported(
          messagePrn, messageType, (short) subMessageId, messageRawData);
      mHardwareGpsNavMessageProto = mGpsNavigationMessageStore.createDecodedNavMessage();
    }
  }

  /** Sets a rough location of the receiver that can be used to request SUPL assistance data */
  public void setReferencePosition(int latE7, int lngE7, int altE7) {
    if (mReferenceLocation == null) {
      mReferenceLocation = new int[3];
    }
    mReferenceLocation[0] = latE7;
    mReferenceLocation[1] = lngE7;
    mReferenceLocation[2] = altE7;
  }

  /**
   * Converts the input from LLA coordinates to ECEF and set up the reference position of {@code
   * mUserPositionVelocityLeastSquareCalculator} to calculate a corrected residual.
   *
   * <p>Based on this input ground truth, true residuals can be computed. This is done by using the
   * high elevation satellites to compute the true user clock error and with the knowledge of the
   * satellite positions.
   *
   * <p>If no ground truth is set, no residual analysis will be performed.
   */
  public void setCorrectedResidualComputationTruthLocationLla(double[] groundTruthLocationLla) {
    if (groundTruthLocationLla == null) {
      mUserPositionVelocityLeastSquareCalculator
          .setTruthLocationForCorrectedResidualComputationEcef(null);
      return;
    }
    GeodeticLlaValues llaValues =
        new GeodeticLlaValues(
            Math.toRadians(groundTruthLocationLla[0]),
            Math.toRadians(groundTruthLocationLla[1]),
            Math.toRadians(groundTruthLocationLla[2]));
    mUserPositionVelocityLeastSquareCalculator.setTruthLocationForCorrectedResidualComputationEcef(
        Lla2EcefConverter.convertFromLlaToEcefMeters(llaValues));
  }

  /** Returns the last computed weighted least square position solution */
  public double[] getPositionSolutionLatLngDeg() {
    return mPositionSolutionLatLngDeg;
  }

  /** Returns the last computed Velocity solution */
  public double[] getVelocitySolutionEnuMps() {
    return mVelocitySolutionEnuMps;
  }

  /**
   * Returns the last computed position and velocity uncertainties in meters and meter per seconds,
   * respectively.
   */
  public double[] getPositionVelocityUncertaintyEnu() {
    return mPositionVelocityUncertaintyEnu;
  }

  /**
   * Returns the pseudorange residuals corrected by using clock bias computed from highest
   * elevationDegree satellites.
   */
  public double[] getPseudorangeResidualsMeters() {
    return mPseudorangeResidualsMeters;
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/PseudorangeSmoother.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import java.util.List;

/**
 * Interface for smoothing a list of {@link GpsMeasurementWithRangeAndUncertainty} instances
 * received at a point of time.
 */
interface PseudorangeSmoother {

  /**
   * Takes an input list of {@link GpsMeasurementWithRangeAndUncertainty} instances and returns a
   * new list that contains smoothed pseudorange measurements.
   *
   * <p>The input list is of size {@link GpsNavigationMessageStore#MAX_NUMBER_OF_SATELLITES} with
   * not visible GPS satellites having null entries, and the returned new list is of the same size.
   *
   * <p>The method does not modify the input list.
   */
  List<GpsMeasurementWithRangeAndUncertainty> updatePseudorangeSmoothingResult(
      List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToGPSReceiverMeasurements);
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/ResidualCorrectionCalculator.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import com.google.common.base.Preconditions;
import com.google.location.lbs.gnss.gps.pseudorange.EcefToTopocentricConverter.TopocentricAEDValues;
import com.google.location.lbs.gnss.gps.pseudorange.UserPositionVelocityWeightedLeastSquare.SatellitesPositionPseudorangesResidualAndCovarianceMatrix;
import java.util.Arrays;
import java.util.Comparator;

/**
 * A tool with the methods to perform the pseudorange residual analysis.
 *
 * <p>The tool allows correcting the pseudorange residuals computed in WLS by removing the user
 * clock error. The user clock bias is computed using the highest elevation satellites as those are
 * assumed not to suffer from multipath. The reported residuals are provided at the input ground
 * truth position by applying an adjustment using the distance of WLS to satellites vs ground-truth
 * to satellites.
 */
public class ResidualCorrectionCalculator {

  /**
   * The threshold for the residual of user clock bias per satellite with respect to the best user
   * clock bias.
   */
  private static final double BEST_USER_CLOCK_BIAS_RESIDUAL_THRESHOLD_METERS = 10;

  /* The number of satellites we pick for calculating the best user clock bias */
  private static final int MIN_SATS_FOR_BIAS_COMPUTATION = 4;

  /**
   * Corrects the pseudorange residual by the best user clock bias estimation computed from the top
   * elevation satellites.
   *
   * @param satellitesPositionPseudorangesResidual satellite position and pseudorange residual info
   *     passed in from WLS
   * @param positionVelocitySolutionECEF position velocity solution passed in from WLS
   * @param groundTruthInputECEFMeters the reference position in ECEF meters
   * @return an array contains the corrected pseudorange residual in meters for each satellite
   */
  public static double[] calculateCorrectedResiduals(
      SatellitesPositionPseudorangesResidualAndCovarianceMatrix
          satellitesPositionPseudorangesResidual,
      double[] positionVelocitySolutionECEF,
      double[] groundTruthInputECEFMeters) {

    double[] residuals = satellitesPositionPseudorangesResidual.pseudorangeResidualsMeters.clone();
    int[] satellitePrn = satellitesPositionPseudorangesResidual.satellitePRNs.clone();
    double[] satelliteElevationDegree = new double[residuals.length];
    SatelliteElevationAndResiduals[] satelliteResidualsListAndElevation =
        new SatelliteElevationAndResiduals[residuals.length];

    // Check the alignment between inputs
    Preconditions.checkArgument(residuals.length == satellitePrn.length);

    // Apply residual corrections per satellite
    for (int i = 0; i < residuals.length; i++) {
      // Calculate the delta of user-satellite distance between ground truth and WLS solution
      // and use the delta to adjust the residuals computed from the WLS. With this adjustments all
      // residuals will be as if they are computed with respect to the ground truth rather than
      // the WLS.
      double[] satellitePos = satellitesPositionPseudorangesResidual.satellitesPositionsMeters[i];
      double wlsUserSatelliteDistance =
          GpsMathOperations.vectorNorm(
              GpsMathOperations.subtractTwoVectors(
                  Arrays.copyOf(positionVelocitySolutionECEF, 3), satellitePos));
      double groundTruthSatelliteDistance =
          GpsMathOperations.vectorNorm(
              GpsMathOperations.subtractTwoVectors(groundTruthInputECEFMeters, satellitePos));

      // Compute the adjustment for satellite i
      double groundTruthAdjustment = wlsUserSatelliteDistance - groundTruthSatelliteDistance;

      // Correct the input residual with the adjustment to ground truth
      residuals[i] = residuals[i] - groundTruthAdjustment;

      // Calculate the elevation in degrees of satellites
      TopocentricAEDValues topocentricAedValues =
          EcefToTopocentricConverter.calculateElAzDistBetween2Points(
              groundTruthInputECEFMeters,
              satellitesPositionPseudorangesResidual.satellitesPositionsMeters[i]);

      satelliteElevationDegree[i] = Math.toDegrees(topocentricAedValues.elevationRadians);

      // Store the computed satellite elevations and residuals into a SatelliteElevationAndResiduals
      // list with clock correction removed.
      satelliteResidualsListAndElevation[i] =
          new SatelliteElevationAndResiduals(
              satelliteElevationDegree[i],
              residuals[i] + positionVelocitySolutionECEF[3],
              satellitePrn[i]);
    }

    double bestUserClockBiasMeters = calculateBestUserClockBias(satelliteResidualsListAndElevation);

    // Use the best clock bias to correct the residuals to ensure that the receiver clock errors are
    // removed from the reported residuals in the analysis
    double[] correctedResidualsMeters =
        GpsMathOperations.createAndFillArray(
            GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES, Double.NaN);

    for (SatelliteElevationAndResiduals element : satelliteResidualsListAndElevation) {
      correctedResidualsMeters[element.svID - 1] = element.residual - bestUserClockBiasMeters;
    }

    return correctedResidualsMeters;
  }

  /**
   * Computes the user clock bias by iteratively averaging the clock bias of top elevation
   * satellites.
   *
   * @param satelliteResidualsAndElevationList a list of satellite elevation and pseudorange
   *     residuals
   * @return the corrected best user clock bias
   */
  private static double calculateBestUserClockBias(
      SatelliteElevationAndResiduals[] satelliteResidualsAndElevationList) {

    // Sort the satellites by descending order of their elevations
    Arrays.sort(
        satelliteResidualsAndElevationList,
        new Comparator<SatelliteElevationAndResiduals>() {
          @Override
          public int compare(SatelliteElevationAndResiduals o1, SatelliteElevationAndResiduals o2) {
            return Double.compare(o2.elevationDegree, o1.elevationDegree);
          }
        });

    // Pick up the top elevation satellites
    double[] topElevationSatsResiduals =
        GpsMathOperations.createAndFillArray(MIN_SATS_FOR_BIAS_COMPUTATION, Double.NaN);
    int numOfUsefulSatsToComputeBias = 0;
    for (int i = 0;
        i < satelliteResidualsAndElevationList.length && i < topElevationSatsResiduals.length;
        i++) {
      topElevationSatsResiduals[i] = satelliteResidualsAndElevationList[i].residual;
      numOfUsefulSatsToComputeBias++;
    }

    double meanResidual;
    double[] deltaResidualFromMean;
    int maxDeltaIndex = -1;

    // Iteratively remove the satellites with highest residuals with respect to the mean of the
    // residuals until the highest residual in the list is below threshold.
    do {
      if (maxDeltaIndex >= 0) {
        topElevationSatsResiduals[maxDeltaIndex] = Double.NaN;
        numOfUsefulSatsToComputeBias--;
      }
      meanResidual = GpsMathOperations.meanOfVector(topElevationSatsResiduals);
      deltaResidualFromMean =
          GpsMathOperations.subtractByScalar(topElevationSatsResiduals, meanResidual);
      maxDeltaIndex = GpsMathOperations.maxIndexOfVector(deltaResidualFromMean);
    } while (deltaResidualFromMean[maxDeltaIndex] > BEST_USER_CLOCK_BIAS_RESIDUAL_THRESHOLD_METERS
        && numOfUsefulSatsToComputeBias > 2);

    return meanResidual;
  }

  /** A container for satellite residual and elevationDegree information */
  private static class SatelliteElevationAndResiduals {
    /** Satellite pseudorange or pseudorange rate residual with clock correction removed */
    final double residual;

    /** Satellite elevation in degrees with respect to the user */
    final double elevationDegree;

    /** Satellite ID */
    final int svID;

    SatelliteElevationAndResiduals(double elevationDegree, double residual, int svID) {
      this.residual = residual;
      this.svID = svID;
      this.elevationDegree = elevationDegree;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/SatelliteClockCorrectionCalculator.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import android.location.cts.nano.Ephemeris.GpsEphemerisProto;

/**
 * Calculates the GPS satellite clock correction based on parameters observed from the navigation
 * message
 *
 * <p>Source: Page 88 - 90 of the ICD-GPS 200
 */
public class SatelliteClockCorrectionCalculator {
  private static final double SPEED_OF_LIGHT_MPS = 299792458.0;
  private static final double EARTH_UNIVERSAL_GRAVITATIONAL_CONSTANT_M3_SM2 = 3.986005e14;
  private static final double RELATIVISTIC_CONSTANT_F = -4.442807633e-10;
  private static final int SECONDS_IN_WEEK = 604800;
  private static final double ACCURACY_TOLERANCE = 1.0e-11;
  private static final int MAX_ITERATIONS = 100;

  /**
   * Computes the GPS satellite clock correction term in meters iteratively following page 88 - 90
   * and 98 - 100 of the ICD GPS 200. The method returns a pair of satellite clock correction in
   * meters and Kepler Eccentric Anomaly in Radians.
   *
   * @param ephemerisProto parameters of the navigation message
   * @param receiverGpsTowAtTimeOfTransmission Receiver estimate of GPS time of week when signal was
   *     transmitted (seconds)
   * @param receiverGpsWeekAtTimeOfTransmission Receiver estimate of GPS week when signal was
   *     transmitted (0-1024+)
   * @throws Exception
   */
  public static SatClockCorrection calculateSatClockCorrAndEccAnomAndTkIteratively(
      GpsEphemerisProto ephemerisProto,
      double receiverGpsTowAtTimeOfTransmission,
      double receiverGpsWeekAtTimeOfTransmission)
      throws Exception {
    // Units are not added in the variable names to have the same name as the ICD-GPS200
    // Mean anomaly (radians)
    double meanAnomalyRad;
    // Kepler's Equation for Eccentric Anomaly iteratively (Radians)
    double eccentricAnomalyRad;
    // Semi-major axis of orbit (meters)
    double a = ephemerisProto.rootOfA * ephemerisProto.rootOfA;
    // Computed mean motion (radians/seconds)
    double n0 = Math.sqrt(EARTH_UNIVERSAL_GRAVITATIONAL_CONSTANT_M3_SM2 / (a * a * a));
    // Corrected mean motion (radians/seconds)
    double n = n0 + ephemerisProto.deltaN;
    // In the following, Receiver GPS week and ephemeris GPS week are used to correct for week
    // rollover when calculating the time from clock reference epoch (tcSec)
    double timeOfTransmissionIncludingRxWeekSec =
        receiverGpsWeekAtTimeOfTransmission * SECONDS_IN_WEEK + receiverGpsTowAtTimeOfTransmission;
    // time from clock reference epoch (seconds) page 88 ICD-GPS200
    double tcSec =
        timeOfTransmissionIncludingRxWeekSec
            - (ephemerisProto.week * SECONDS_IN_WEEK + ephemerisProto.toc);
    // Correction for week rollover
    tcSec = fixWeekRollover(tcSec);
    double oldEccentricAnomalyRad = 0.0;
    double newSatClockCorrectionSeconds = 0.0;
    double relativisticCorrection = 0.0;
    double changeInSatClockCorrection = 0.0;
    // Initial satellite clock correction (unknown relativistic correction). Iterate to correct
    // with the relativistic effect and obtain a stable
    final double initSatClockCorrectionSeconds =
        ephemerisProto.af0
            + ephemerisProto.af1 * tcSec
            + ephemerisProto.af2 * tcSec * tcSec
            - ephemerisProto.tgd;
    double satClockCorrectionSeconds = initSatClockCorrectionSeconds;
    double tkSec;
    int satClockCorrectionsCounter = 0;
    do {
      int eccentricAnomalyCounter = 0;
      // time from ephemeris reference epoch (seconds) page 98 ICD-GPS200
      tkSec =
          timeOfTransmissionIncludingRxWeekSec
              - (ephemerisProto.week * SECONDS_IN_WEEK
                  + ephemerisProto.toe
                  + satClockCorrectionSeconds);
      // Correction for week rollover
      tkSec = fixWeekRollover(tkSec);
      // Mean anomaly (radians)
      meanAnomalyRad = ephemerisProto.m0 + n * tkSec;
      // eccentric anomaly (radians)
      eccentricAnomalyRad = meanAnomalyRad;
      // Iteratively solve for Kepler's eccentric anomaly according to ICD-GPS200 page 99
      do {
        oldEccentricAnomalyRad = eccentricAnomalyRad;
        eccentricAnomalyRad = meanAnomalyRad + ephemerisProto.e * Math.sin(eccentricAnomalyRad);
        eccentricAnomalyCounter++;
        if (eccentricAnomalyCounter > MAX_ITERATIONS) {
          throw new Exception(
              "Kepler Eccentric Anomaly calculation did not converge in "
                  + MAX_ITERATIONS
                  + " iterations");
        }
      } while (Math.abs(oldEccentricAnomalyRad - eccentricAnomalyRad) > ACCURACY_TOLERANCE);
      // relativistic correction term (seconds)
      relativisticCorrection =
          RELATIVISTIC_CONSTANT_F
              * ephemerisProto.e
              * ephemerisProto.rootOfA
              * Math.sin(eccentricAnomalyRad);
      // satellite clock correction including relativistic effect
      newSatClockCorrectionSeconds = initSatClockCorrectionSeconds + relativisticCorrection;
      changeInSatClockCorrection =
          Math.abs(satClockCorrectionSeconds - newSatClockCorrectionSeconds);
      satClockCorrectionSeconds = newSatClockCorrectionSeconds;
      satClockCorrectionsCounter++;
      if (satClockCorrectionsCounter > MAX_ITERATIONS) {
        throw new Exception(
            "Satellite Clock Correction calculation did not converge in "
                + MAX_ITERATIONS
                + " iterations");
      }
    } while (changeInSatClockCorrection > ACCURACY_TOLERANCE);
    tkSec =
        timeOfTransmissionIncludingRxWeekSec
            - (ephemerisProto.week * SECONDS_IN_WEEK
                + ephemerisProto.toe
                + satClockCorrectionSeconds);
    // return satellite clock correction (meters) and Kepler Eccentric Anomaly in Radians
    return new SatClockCorrection(
        satClockCorrectionSeconds * SPEED_OF_LIGHT_MPS, eccentricAnomalyRad, tkSec);
  }

  /**
   * Calculates Satellite Clock Error Rate in (meters/second) by subtracting the Satellite Clock
   * Error Values at t+0.5s and t-0.5s.
   *
   * <p>This approximation is more accurate than differentiating because both the orbital and
   * relativity terms have non-linearities that are not easily differentiable.
   */
  public static double calculateSatClockCorrErrorRate(
      GpsEphemerisProto ephemerisProto,
      double receiverGpsTowAtTimeOfTransmissionSeconds,
      double receiverGpsWeekAtTimeOfTransmission)
      throws Exception {
    SatClockCorrection satClockCorrectionPlus =
        calculateSatClockCorrAndEccAnomAndTkIteratively(
            ephemerisProto,
            receiverGpsTowAtTimeOfTransmissionSeconds + 0.5,
            receiverGpsWeekAtTimeOfTransmission);
    SatClockCorrection satClockCorrectionMinus =
        calculateSatClockCorrAndEccAnomAndTkIteratively(
            ephemerisProto,
            receiverGpsTowAtTimeOfTransmissionSeconds - 0.5,
            receiverGpsWeekAtTimeOfTransmission);
    double satelliteClockErrorRate =
        satClockCorrectionPlus.satelliteClockCorrectionMeters
            - satClockCorrectionMinus.satelliteClockCorrectionMeters;
    return satelliteClockErrorRate;
  }

  /**
   * Method to check for week rollover according to ICD-GPS 200 page 98.
   *
   * <p>Result should be between -302400 and 302400 if the ephemeris is within one week of
   * transmission, otherwise it is adjusted to the correct range
   */
  private static double fixWeekRollover(double time) {
    double correctedTime = time;
    if (time > SECONDS_IN_WEEK / 2.0) {
      correctedTime = time - SECONDS_IN_WEEK;
    }
    if (time < -SECONDS_IN_WEEK / 2.0) {
      correctedTime = time + SECONDS_IN_WEEK;
    }
    return correctedTime;
  }

  /**
   * Class containing the satellite clock correction parameters: The satellite clock correction in
   * meters, Kepler Eccentric Anomaly in Radians and the time from the reference epoch in seconds.
   */
  public static class SatClockCorrection {
    /** Satellite clock correction in meters */
    public final double satelliteClockCorrectionMeters;
    /** Kepler Eccentric Anomaly in Radians */
    public final double eccentricAnomalyRadians;
    /** Time from the reference epoch in Seconds */
    public final double timeFromRefEpochSec;

    /** Constructor */
    public SatClockCorrection(
        double satelliteClockCorrectionMeters,
        double eccentricAnomalyRadians,
        double timeFromRefEpochSec) {
      this.satelliteClockCorrectionMeters = satelliteClockCorrectionMeters;
      this.eccentricAnomalyRadians = eccentricAnomalyRadians;
      this.timeFromRefEpochSec = timeFromRefEpochSec;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/SatellitePositionCalculator.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import android.location.cts.nano.Ephemeris.GpsEphemerisProto;
import com.google.location.lbs.gnss.gps.pseudorange.SatelliteClockCorrectionCalculator.SatClockCorrection;

/** Class to calculate GPS satellite positions from the ephemeris data */
public class SatellitePositionCalculator {
  private static final double SPEED_OF_LIGHT_MPS = 299792458.0;
  private static final double UNIVERSAL_GRAVITATIONAL_PARAMETER_M3_SM2 = 3.986005e14;
  private static final int NUMBER_OF_ITERATIONS_FOR_SAT_POS_CALCULATION = 5;
  private static final double EARTH_ROTATION_RATE_RAD_PER_SEC = 7.2921151467e-5;

  /**
   * Calculates GPS satellite position and velocity from ephemeris including the Sagnac effect
   * starting from unknown user to satellite distance and speed. So we start from an initial guess
   * of the user to satellite range and range rate and iterate to include the Sagnac effect. Few
   * iterations are enough to achieve a satellite position with millimeter accuracy. A {@code
   * PositionAndVelocity} class is returned containing satellite position in meters (x, y and z) and
   * velocity in meters per second (x, y, z)
   *
   * <p>Satellite position and velocity equations are obtained from:
   * http://www.gps.gov/technical/icwg/ICD-GPS-200C.pdf) pages 94 - 101 and
   * http://fenrir.naruoka.org/download/autopilot/note/080205_gps/gps_velocity.pdf
   *
   * @param ephemerisProto parameters of the navigation message
   * @param receiverGpsTowAtTimeOfTransmissionCorrectedSec Receiver estimate of GPS time of week
   *     when signal was transmitted corrected with the satellite clock drift (seconds)
   * @param receiverGpsWeekAtTimeOfTransmission Receiver estimate of GPS week when signal was
   *     transmitted (0-1024+)
   * @param userPosXMeters Last known user x-position (if known) [meters]
   * @param userPosYMeters Last known user y-position (if known) [meters]
   * @param userPosZMeters Last known user z-position (if known) [meters]
   * @throws Exception
   */
  public static PositionAndVelocity calculateSatellitePositionAndVelocityFromEphemeris(
      GpsEphemerisProto ephemerisProto,
      double receiverGpsTowAtTimeOfTransmissionCorrectedSec,
      int receiverGpsWeekAtTimeOfTransmission,
      double userPosXMeters,
      double userPosYMeters,
      double userPosZMeters)
      throws Exception {

    // lets start with a first user to sat distance guess of 70 ms and zero velocity
    RangeAndRangeRate userSatRangeAndRate =
        new RangeAndRangeRate(0.070 * SPEED_OF_LIGHT_MPS, 0.0 /* range rate*/);

    // To apply sagnac effect correction, We are starting from an approximate guess of the user to
    // satellite range, iterate 3 times and that should be enough to reach millimeter accuracy
    PositionAndVelocity satPosAndVel = new PositionAndVelocity(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    PositionAndVelocity userPosAndVel =
        new PositionAndVelocity(
            userPosXMeters,
            userPosYMeters,
            userPosZMeters,
            0.0 /* user velocity x*/,
            0.0 /* user velocity y*/,
            0.0 /* user velocity z */);
    for (int i = 0; i < NUMBER_OF_ITERATIONS_FOR_SAT_POS_CALCULATION; i++) {
      calculateSatellitePositionAndVelocity(
          ephemerisProto,
          receiverGpsTowAtTimeOfTransmissionCorrectedSec,
          receiverGpsWeekAtTimeOfTransmission,
          userSatRangeAndRate,
          satPosAndVel);
      computeUserToSatelliteRangeAndRangeRate(userPosAndVel, satPosAndVel, userSatRangeAndRate);
    }
    return satPosAndVel;
  }

  /**
   * Calculates GPS satellite position and velocity from ephemeris based on the ICD-GPS-200.
   * Satellite position in meters (x, y and z) and velocity in meters per second (x, y, z) are set
   * in the passed {@code PositionAndVelocity} instance.
   *
   * <p>Sources: http://www.gps.gov/technical/icwg/ICD-GPS-200C.pdf) pages 94 - 101 and
   * http://fenrir.naruoka.org/download/autopilot/note/080205_gps/gps_velocity.pdf
   *
   * @param ephemerisProto parameters of the navigation message
   * @param receiverGpsTowAtTimeOfTransmissionCorrected Receiver estimate of GPS time of week when
   *     signal was transmitted corrected with the satellite clock drift (seconds)
   * @param receiverGpsWeekAtTimeOfTransmission Receiver estimate of GPS week when signal was
   *     transmitted (0-1024+)
   * @param userSatRangeAndRate user to satellite range and range rate
   * @param satPosAndVel Satellite position and velocity instance in which the method results will
   *     be set
   * @throws Exception
   */
  public static void calculateSatellitePositionAndVelocity(
      GpsEphemerisProto ephemerisProto,
      double receiverGpsTowAtTimeOfTransmissionCorrected,
      int receiverGpsWeekAtTimeOfTransmission,
      RangeAndRangeRate userSatRangeAndRate,
      PositionAndVelocity satPosAndVel)
      throws Exception {

    // Calculate satellite clock correction (meters), Kepler Eccentric anomaly (radians) and time
    // from ephemeris reference epoch (tkSec) iteratively
    SatClockCorrection satClockCorrectionValues =
        SatelliteClockCorrectionCalculator.calculateSatClockCorrAndEccAnomAndTkIteratively(
            ephemerisProto,
            receiverGpsTowAtTimeOfTransmissionCorrected,
            receiverGpsWeekAtTimeOfTransmission);

    double eccentricAnomalyRadians = satClockCorrectionValues.eccentricAnomalyRadians;
    double tkSec = satClockCorrectionValues.timeFromRefEpochSec;

    // True_anomaly (angle from perigee)
    double trueAnomalyRadians =
        Math.atan2(
            Math.sqrt(1.0 - ephemerisProto.e * ephemerisProto.e)
                * Math.sin(eccentricAnomalyRadians),
            Math.cos(eccentricAnomalyRadians) - ephemerisProto.e);

    // Argument of latitude of the satellite
    double argumentOfLatitudeRadians = trueAnomalyRadians + ephemerisProto.omega;

    // Radius of satellite orbit
    double radiusOfSatelliteOrbitMeters =
        ephemerisProto.rootOfA
            * ephemerisProto.rootOfA
            * (1.0 - ephemerisProto.e * Math.cos(eccentricAnomalyRadians));

    // Radius correction due to second harmonic perturbations of the orbit
    double radiusCorrectionMeters =
        ephemerisProto.crc * Math.cos(2.0 * argumentOfLatitudeRadians)
            + ephemerisProto.crs * Math.sin(2.0 * argumentOfLatitudeRadians);
    // Argument of latitude correction due to second harmonic perturbations of the orbit
    double argumentOfLatitudeCorrectionRadians =
        ephemerisProto.cuc * Math.cos(2.0 * argumentOfLatitudeRadians)
            + ephemerisProto.cus * Math.sin(2.0 * argumentOfLatitudeRadians);
    // Correction to inclination due to second harmonic perturbations of the orbit
    double inclinationCorrectionRadians =
        ephemerisProto.cic * Math.cos(2.0 * argumentOfLatitudeRadians)
            + ephemerisProto.cis * Math.sin(2.0 * argumentOfLatitudeRadians);

    // Corrected radius of satellite orbit
    radiusOfSatelliteOrbitMeters += radiusCorrectionMeters;
    // Corrected argument of latitude
    argumentOfLatitudeRadians += argumentOfLatitudeCorrectionRadians;
    // Corrected inclination
    double inclinationRadians =
        ephemerisProto.i0 + inclinationCorrectionRadians + ephemerisProto.iDot * tkSec;

    // Position in orbital plane
    double xPositionMeters = radiusOfSatelliteOrbitMeters * Math.cos(argumentOfLatitudeRadians);
    double yPositionMeters = radiusOfSatelliteOrbitMeters * Math.sin(argumentOfLatitudeRadians);

    // Corrected longitude of the ascending node (signal propagation time is included to compensate
    // for the Sagnac effect)
    double omegaKRadians =
        ephemerisProto.omega0
            + (ephemerisProto.omegaDot - EARTH_ROTATION_RATE_RAD_PER_SEC) * tkSec
            - EARTH_ROTATION_RATE_RAD_PER_SEC
                * (ephemerisProto.toe + userSatRangeAndRate.rangeMeters / SPEED_OF_LIGHT_MPS);

    // compute the resulting satellite position
    double satPosXMeters =
        xPositionMeters * Math.cos(omegaKRadians)
            - yPositionMeters * Math.cos(inclinationRadians) * Math.sin(omegaKRadians);
    double satPosYMeters =
        xPositionMeters * Math.sin(omegaKRadians)
            + yPositionMeters * Math.cos(inclinationRadians) * Math.cos(omegaKRadians);
    double satPosZMeters = yPositionMeters * Math.sin(inclinationRadians);

    // Satellite Velocity Computation using the broadcast ephemeris
    // http://fenrir.naruoka.org/download/autopilot/note/080205_gps/gps_velocity.pdf
    // Units are not added in some of the variable names to have the same name as the ICD-GPS200
    // Semi-major axis of orbit (meters)
    double a = ephemerisProto.rootOfA * ephemerisProto.rootOfA;
    // Computed mean motion (radians/seconds)
    double n0 = Math.sqrt(UNIVERSAL_GRAVITATIONAL_PARAMETER_M3_SM2 / (a * a * a));
    // Corrected mean motion (radians/seconds)
    double n = n0 + ephemerisProto.deltaN;
    // Derivative of mean anomaly (radians/seconds)
    double meanAnomalyDotRadPerSec = n;
    // Derivative of eccentric anomaly (radians/seconds)
    double eccentricAnomalyDotRadPerSec =
        meanAnomalyDotRadPerSec / (1.0 - ephemerisProto.e * Math.cos(eccentricAnomalyRadians));
    // Derivative of true anomaly (radians/seconds)
    double trueAnomalyDotRadPerSec =
        Math.sin(eccentricAnomalyRadians)
            * eccentricAnomalyDotRadPerSec
            * (1.0 + ephemerisProto.e * Math.cos(trueAnomalyRadians))
            / (Math.sin(trueAnomalyRadians)
                * (1.0 - ephemerisProto.e * Math.cos(eccentricAnomalyRadians)));
    // Derivative of argument of latitude (radians/seconds)
    double argumentOfLatitudeDotRadPerSec =
        trueAnomalyDotRadPerSec
            + 2.0
                * (ephemerisProto.cus * Math.cos(2.0 * argumentOfLatitudeRadians)
                    - ephemerisProto.cuc * Math.sin(2.0 * argumentOfLatitudeRadians))
                * trueAnomalyDotRadPerSec;
    // Derivative of radius of satellite orbit (m/s)
    double radiusOfSatelliteOrbitDotMPerSec =
        a
                * ephemerisProto.e
                * Math.sin(eccentricAnomalyRadians)
                * n
                / (1.0 - ephemerisProto.e * Math.cos(eccentricAnomalyRadians))
            + 2.0
                * (ephemerisProto.crs * Math.cos(2.0 * argumentOfLatitudeRadians)
                    - ephemerisProto.crc * Math.sin(2.0 * argumentOfLatitudeRadians))
                * trueAnomalyDotRadPerSec;
    // Derivative of the inclination (radians/seconds)
    double inclinationDotRadPerSec =
        ephemerisProto.iDot
            + (ephemerisProto.cis * Math.cos(2.0 * argumentOfLatitudeRadians)
                    - ephemerisProto.cic * Math.sin(2.0 * argumentOfLatitudeRadians))
                * 2.0
                * trueAnomalyDotRadPerSec;

    double xVelocityMPS =
        radiusOfSatelliteOrbitDotMPerSec * Math.cos(argumentOfLatitudeRadians)
            - yPositionMeters * argumentOfLatitudeDotRadPerSec;
    double yVelocityMPS =
        radiusOfSatelliteOrbitDotMPerSec * Math.sin(argumentOfLatitudeRadians)
            + xPositionMeters * argumentOfLatitudeDotRadPerSec;

    // Corrected rate of right ascension including compensation for the Sagnac effect
    double omegaDotRadPerSec =
        ephemerisProto.omegaDot
            - EARTH_ROTATION_RATE_RAD_PER_SEC
                * (1.0 + userSatRangeAndRate.rangeRateMetersPerSec / SPEED_OF_LIGHT_MPS);
    // compute the resulting satellite velocity
    double satVelXMPS =
        (xVelocityMPS - yPositionMeters * Math.cos(inclinationRadians) * omegaDotRadPerSec)
                * Math.cos(omegaKRadians)
            - (xPositionMeters * omegaDotRadPerSec
                    + yVelocityMPS * Math.cos(inclinationRadians)
                    - yPositionMeters * Math.sin(inclinationRadians) * inclinationDotRadPerSec)
                * Math.sin(omegaKRadians);
    double satVelYMPS =
        (xVelocityMPS - yPositionMeters * Math.cos(inclinationRadians) * omegaDotRadPerSec)
                * Math.sin(omegaKRadians)
            + (xPositionMeters * omegaDotRadPerSec
                    + yVelocityMPS * Math.cos(inclinationRadians)
                    - yPositionMeters * Math.sin(inclinationRadians) * inclinationDotRadPerSec)
                * Math.cos(omegaKRadians);
    double satVelZMPS =
        yVelocityMPS * Math.sin(inclinationRadians)
            + yPositionMeters * Math.cos(inclinationRadians) * inclinationDotRadPerSec;

    satPosAndVel.positionXMeters = satPosXMeters;
    satPosAndVel.positionYMeters = satPosYMeters;
    satPosAndVel.positionZMeters = satPosZMeters;
    satPosAndVel.velocityXMetersPerSec = satVelXMPS;
    satPosAndVel.velocityYMetersPerSec = satVelYMPS;
    satPosAndVel.velocityZMetersPerSec = satVelZMPS;
  }

  /**
   * Computes and sets the passed {@code RangeAndRangeRate} instance containing user to satellite
   * range (meters) and range rate (m/s) given the user position (ECEF meters), user velocity (m/s),
   * satellite position (ECEF meters) and satellite velocity (m/s).
   */
  private static void computeUserToSatelliteRangeAndRangeRate(
      PositionAndVelocity userPosAndVel,
      PositionAndVelocity satPosAndVel,
      RangeAndRangeRate rangeAndRangeRate) {
    double dXMeters = satPosAndVel.positionXMeters - userPosAndVel.positionXMeters;
    double dYMeters = satPosAndVel.positionYMeters - userPosAndVel.positionYMeters;
    double dZMeters = satPosAndVel.positionZMeters - userPosAndVel.positionZMeters;
    // range in meters
    double rangeMeters = Math.sqrt(dXMeters * dXMeters + dYMeters * dYMeters + dZMeters * dZMeters);
    // range rate in meters / second
    double rangeRateMetersPerSec =
        ((userPosAndVel.velocityXMetersPerSec - satPosAndVel.velocityXMetersPerSec) * dXMeters
                + (userPosAndVel.velocityYMetersPerSec - satPosAndVel.velocityYMetersPerSec)
                    * dYMeters
                + (userPosAndVel.velocityZMetersPerSec - satPosAndVel.velocityZMetersPerSec)
                    * dZMeters)
            / rangeMeters;
    rangeAndRangeRate.rangeMeters = rangeMeters;
    rangeAndRangeRate.rangeRateMetersPerSec = rangeRateMetersPerSec;
  }

  /**
   * A class containing position values (x, y, z) in meters and velocity values (x, y, z) in meters
   * per seconds
   */
  public static class PositionAndVelocity {
    /** x - position in meters */
    public double positionXMeters;
    /** y - position in meters */
    public double positionYMeters;
    /** z - position in meters */
    public double positionZMeters;
    /** x - velocity in meters */
    public double velocityXMetersPerSec;
    /** y - velocity in meters */
    public double velocityYMetersPerSec;
    /** z - velocity in meters */
    public double velocityZMetersPerSec;

    /** Constructor */
    public PositionAndVelocity(
        double positionXMeters,
        double positionYMeters,
        double positionZMeters,
        double velocityXMetersPerSec,
        double velocityYMetersPerSec,
        double velocityZMetersPerSec) {
      this.positionXMeters = positionXMeters;
      this.positionYMeters = positionYMeters;
      this.positionZMeters = positionZMeters;
      this.velocityXMetersPerSec = velocityXMetersPerSec;
      this.velocityYMetersPerSec = velocityYMetersPerSec;
      this.velocityZMetersPerSec = velocityZMetersPerSec;
    }
  }

  /**
   * A class containing range of satellite to user in meters and range rate in meters per seconds
   */
  public static class RangeAndRangeRate {
    /** Range in meters */
    public double rangeMeters;
    /** Range rate in meters per seconds */
    public double rangeRateMetersPerSec;

    /** Constructor */
    public RangeAndRangeRate(double rangeMeters, double rangeRateMetersPerSec) {
      this.rangeMeters = rangeMeters;
      this.rangeRateMetersPerSec = rangeRateMetersPerSec;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/TroposphericModelEgnos.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

/**
 * Calculate the tropospheric delay based on the ENGOS Tropospheric model.
 *
 * <p>The tropospheric delay is modeled as a combined effect of the delay experienced due to
 * hydrostatic (dry) and wet components of the troposphere. Both delays experienced at zenith are
 * scaled with a mapping function to get the delay at any specific elevation.
 *
 * <p>The tropospheric model algorithm of EGNOS model by Penna, N., A. Dodson and W. Chen (2001)
 * (http://espace.library.curtin.edu.au/cgi-bin/espace.pdf?file=/2008/11/13/file_1/18917) is used
 * for calculating the zenith delays. In this model, the weather parameters are extracted using
 * interpolation from lookup table derived from the US Standard Atmospheric Supplements, 1966.
 *
 * <p>A close form mapping function is built using Guo and Langley, 2003
 * (http://gauss2.gge.unb.ca/papers.pdf/iongpsgnss2003.guo.pdf) which is able to calculate accurate
 * mapping down to 2 degree elevations.
 *
 * <p>Sources:
 *
 * <p>http://espace.library.curtin.edu.au/cgi-bin/espace.pdf?file=/2008/11/13/file_1/18917
 *
 * <p>- http://www.academia.edu/3512180/Assessment_of_UNB3M_neutral
 * _atmosphere_model_and_EGNOS_model_for_near-equatorial-tropospheric_delay_correction
 *
 * <p>- http://gauss.gge.unb.ca/papers.pdf/ion52am.collins.pdf
 *
 * <p>- http://www.navipedia.net/index.php/Tropospheric_Delay#cite_ref-3
 *
 * <p>Hydrostatic and non-hydrostatic mapping functions are obtained from:
 * http://gauss2.gge.unb.ca/papers.pdf/iongpsgnss2003.guo.pdf
 */
public class TroposphericModelEgnos {
  // parameters of the EGNOS models
  private static final int INDEX_15_DEGREES = 0;
  private static final int INDEX_75_DEGREES = 4;
  private static final int LATITUDE_15_DEGREES = 15;
  private static final int LATITUDE_75_DEGREES = 75;
  // Lookup Average parameters
  // Troposphere average pressure mbar
  private static final double[] latDegreeToPressureMbarAvgMap = {
    1013.25, 1017.25, 1015.75, 1011.75, 1013.0
  };
  // Troposphere average temperature Kelvin
  private static final double[] latDegreeToTempKelvinAvgMap = {
    299.65, 294.15, 283.15, 272.15, 263.65
  };
  // Troposphere average water vapor pressure
  private static final double[] latDegreeToWVPressureMbarAvgMap = {26.31, 21.79, 11.66, 6.78, 4.11};
  // Troposphere average temperature lapse rate K/m
  private static final double[] latDegreeToBetaAvgMapKPM = {
    6.30e-3, 6.05e-3, 5.58e-3, 5.39e-3, 4.53e-3
  };
  // Troposphere average water vapor lapse rate (dimensionless)
  private static final double[] latDegreeToLambdaAvgMap = {2.77, 3.15, 2.57, 1.81, 1.55};

  // Lookup Amplitude parameters
  // Troposphere amplitude pressure mbar
  private static final double[] latDegreeToPressureMbarAmpMap = {0.0, -3.75, -2.25, -1.75, -0.5};
  // Troposphere amplitude temperature Kelvin
  private static final double[] latDegreeToTempKelvinAmpMap = {0.0, 7.0, 11.0, 15.0, 14.5};
  // Troposphere amplitude water vapor pressure
  private static final double[] latDegreeToWVPressureMbarAmpMap = {0.0, 8.85, 7.24, 5.36, 3.39};
  // Troposphere amplitude temperature lapse rate K/m
  private static final double[] latDegreeToBetaAmpMapKPM = {
    0.0, 0.25e-3, 0.32e-3, 0.81e-3, 0.62e-3
  };
  // Troposphere amplitude water vapor lapse rate (dimensionless)
  private static final double[] latDegreeToLambdaAmpMap = {0.0, 0.33, 0.46, 0.74, 0.30};
  // Zenith delay dry constant K/mbar
  private static final double K1 = 77.604;
  // Zenith delay wet constant K^2/mbar
  private static final double K2 = 382000.0;
  // gas constant for dry air J/kg/K
  private static final double RD = 287.054;
  // Acceleration of gravity at the atmospheric column centroid m/s^-2
  private static final double GM = 9.784;
  // Gravity m/s^2
  private static final double GRAVITY_MPS2 = 9.80665;

  private static final double MINIMUM_INTERPOLATION_THRESHOLD = 1e-25;
  private static final double B_HYDROSTATIC = 0.0035716;
  private static final double C_HYDROSTATIC = 0.082456;
  private static final double B_NON_HYDROSTATIC = 0.0018576;
  private static final double C_NON_HYDROSTATIC = 0.062741;
  private static final double SOUTHERN_HEMISPHERE_DMIN = 211.0;
  private static final double NORTHERN_HEMISPHERE_DMIN = 28.0;
  // Days recalling that every fourth year is a leap year and has an extra day - February 29th
  private static final double DAYS_PER_YEAR = 365.25;

  /**
   * Computes the tropospheric correction in meters given the satellite elevation in radians, the
   * user latitude in radians, the user Orthometric height above sea level in meters and the day of
   * the year.
   *
   * <p>Dry and wet delay zenith delay components are calculated and then scaled with the mapping
   * function at the given satellite elevation.
   */
  public static double calculateTropoCorrectionMeters(
      double satElevationRadians,
      double userLatitudeRadian,
      double heightMetersAboveSeaLevel,
      int dayOfYear1To366) {
    DryAndWetMappingValues dryAndWetMappingValues =
        computeDryAndWetMappingValuesUsingUNBabcMappingFunction(
            satElevationRadians, userLatitudeRadian, heightMetersAboveSeaLevel);
    DryAndWetZenithDelays dryAndWetZenithDelays =
        calculateZenithDryAndWetDelaysSec(
            userLatitudeRadian, heightMetersAboveSeaLevel, dayOfYear1To366);

    double drydelaySeconds =
        dryAndWetZenithDelays.dryZenithDelaySec * dryAndWetMappingValues.dryMappingValue;
    double wetdelaySeconds =
        dryAndWetZenithDelays.wetZenithDelaySec * dryAndWetMappingValues.wetMappingValue;
    return drydelaySeconds + wetdelaySeconds;
  }

  /**
   * Computes the dry and wet mapping values based on the University of Brunswick UNBabc model. The
   * mapping function inputs are satellite elevation in radians, user latitude in radians and user
   * orthometric height above sea level in meters. The function returns {@code
   * DryAndWetMappingValues} containing dry and wet mapping values.
   *
   * <p>From the many dry and wet mapping functions of components of the troposphere, the method
   * from the University of Brunswick in Canada was selected due to its reasonable computation time
   * and accuracy with satellites as low as 2 degrees elevation.
   *
   * <p>Source: http://gauss2.gge.unb.ca/papers.pdf/iongpsgnss2003.guo.pdf
   */
  private static DryAndWetMappingValues computeDryAndWetMappingValuesUsingUNBabcMappingFunction(
      double satElevationRadians, double userLatitudeRadians, double heightMetersAboveSeaLevel) {

    if (satElevationRadians > Math.PI / 2.0) {
      satElevationRadians = Math.PI / 2.0;
    } else if (satElevationRadians < 2.0 * Math.PI / 180.0) {
      satElevationRadians = Math.toRadians(2.0);
    }

    // dry components mapping parameters
    double aHydrostatic =
        (1.18972
                - 0.026855 * heightMetersAboveSeaLevel / 1000.0
                + 0.10664 * Math.cos(userLatitudeRadians))
            / 1000.0;

    double numeratorDry = 1.0 + (aHydrostatic / (1.0 + (B_HYDROSTATIC / (1.0 + C_HYDROSTATIC))));
    double denominatorDry =
        Math.sin(satElevationRadians)
            + (aHydrostatic
                / (Math.sin(satElevationRadians)
                    + (B_HYDROSTATIC / (Math.sin(satElevationRadians) + C_HYDROSTATIC))));

    double drymap = numeratorDry / denominatorDry;

    // wet components mapping parameters
    double aNonHydrostatic =
        (0.61120
                - 0.035348 * heightMetersAboveSeaLevel / 1000.0
                - 0.01526 * Math.cos(userLatitudeRadians))
            / 1000.0;

    double numeratorWet =
        1.0 + (aNonHydrostatic / (1.0 + (B_NON_HYDROSTATIC / (1.0 + C_NON_HYDROSTATIC))));
    double denominatorWet =
        Math.sin(satElevationRadians)
            + (aNonHydrostatic
                / (Math.sin(satElevationRadians)
                    + (B_NON_HYDROSTATIC / (Math.sin(satElevationRadians) + C_NON_HYDROSTATIC))));

    double wetmap = numeratorWet / denominatorWet;
    return new DryAndWetMappingValues(drymap, wetmap);
  }

  /**
   * Computes the combined effect of the delay at zenith experienced due to hydrostatic (dry) and
   * wet components of the troposphere. The function inputs are the user latitude in radians, user
   * orthometric height above sea level in meters and the day of the year (1-366). The function
   * returns a {@code DryAndWetZenithDelays} containing dry and wet delays at zenith.
   *
   * <p>EGNOS Tropospheric model by Penna et al. (2001) is used in this case.
   * (http://espace.library.curtin.edu.au/cgi-bin/espace.pdf?file=/2008/11/13/file_1/18917)
   */
  private static DryAndWetZenithDelays calculateZenithDryAndWetDelaysSec(
      double userLatitudeRadians, double heightMetersAboveSeaLevel, int dayOfYear1To366) {
    // interpolated meteorological values
    double pressureMbar;
    double tempKelvin;
    double waterVaporPressureMbar;
    // temperature lapse rate, [K/m]
    double beta;
    // water vapor lapse rate, dimensionless
    double lambda;

    double absLatitudeDeg = Math.toDegrees(Math.abs(userLatitudeRadians));
    // day of year min constant
    double dmin;
    if (userLatitudeRadians < 0) {
      dmin = SOUTHERN_HEMISPHERE_DMIN;
    } else {
      dmin = NORTHERN_HEMISPHERE_DMIN;
    }
    double amplitudeScaleFactor =
        Math.cos((2 * Math.PI * (dayOfYear1To366 - dmin)) / DAYS_PER_YEAR);

    if (absLatitudeDeg <= LATITUDE_15_DEGREES) {
      pressureMbar =
          latDegreeToPressureMbarAvgMap[INDEX_15_DEGREES]
              - latDegreeToPressureMbarAmpMap[INDEX_15_DEGREES] * amplitudeScaleFactor;
      tempKelvin =
          latDegreeToTempKelvinAvgMap[INDEX_15_DEGREES]
              - latDegreeToTempKelvinAmpMap[INDEX_15_DEGREES] * amplitudeScaleFactor;
      waterVaporPressureMbar =
          latDegreeToWVPressureMbarAvgMap[INDEX_15_DEGREES]
              - latDegreeToWVPressureMbarAmpMap[INDEX_15_DEGREES] * amplitudeScaleFactor;
      beta =
          latDegreeToBetaAvgMapKPM[INDEX_15_DEGREES]
              - latDegreeToBetaAmpMapKPM[INDEX_15_DEGREES] * amplitudeScaleFactor;
      lambda =
          latDegreeToLambdaAmpMap[INDEX_15_DEGREES]
              - latDegreeToLambdaAmpMap[INDEX_15_DEGREES] * amplitudeScaleFactor;
    } else if (absLatitudeDeg > LATITUDE_15_DEGREES && absLatitudeDeg < LATITUDE_75_DEGREES) {
      int key = (int) (absLatitudeDeg / LATITUDE_15_DEGREES);

      double averagePressureMbar =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToPressureMbarAvgMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToPressureMbarAvgMap[key],
              absLatitudeDeg);
      double amplitudePressureMbar =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToPressureMbarAmpMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToPressureMbarAmpMap[key],
              absLatitudeDeg);
      pressureMbar = averagePressureMbar - amplitudePressureMbar * amplitudeScaleFactor;

      double averageTempKelvin =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToTempKelvinAvgMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToTempKelvinAvgMap[key],
              absLatitudeDeg);
      double amplitudeTempKelvin =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToTempKelvinAmpMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToTempKelvinAmpMap[key],
              absLatitudeDeg);
      tempKelvin = averageTempKelvin - amplitudeTempKelvin * amplitudeScaleFactor;

      double averageWaterVaporPressureMbar =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToWVPressureMbarAvgMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToWVPressureMbarAvgMap[key],
              absLatitudeDeg);
      double amplitudeWaterVaporPressureMbar =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToWVPressureMbarAmpMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToWVPressureMbarAmpMap[key],
              absLatitudeDeg);
      waterVaporPressureMbar =
          averageWaterVaporPressureMbar - amplitudeWaterVaporPressureMbar * amplitudeScaleFactor;

      double averageBeta =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToBetaAvgMapKPM[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToBetaAvgMapKPM[key],
              absLatitudeDeg);
      double amplitudeBeta =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToBetaAmpMapKPM[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToBetaAmpMapKPM[key],
              absLatitudeDeg);
      beta = averageBeta - amplitudeBeta * amplitudeScaleFactor;

      double averageLambda =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToLambdaAvgMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToLambdaAvgMap[key],
              absLatitudeDeg);
      double amplitudeLambda =
          interpolate(
              key * LATITUDE_15_DEGREES,
              latDegreeToLambdaAmpMap[key - 1],
              (key + 1) * LATITUDE_15_DEGREES,
              latDegreeToLambdaAmpMap[key],
              absLatitudeDeg);
      lambda = averageLambda - amplitudeLambda * amplitudeScaleFactor;
    } else {
      pressureMbar =
          latDegreeToPressureMbarAvgMap[INDEX_75_DEGREES]
              - latDegreeToPressureMbarAmpMap[INDEX_75_DEGREES] * amplitudeScaleFactor;
      tempKelvin =
          latDegreeToTempKelvinAvgMap[INDEX_75_DEGREES]
              - latDegreeToTempKelvinAmpMap[INDEX_75_DEGREES] * amplitudeScaleFactor;
      waterVaporPressureMbar =
          latDegreeToWVPressureMbarAvgMap[INDEX_75_DEGREES]
              - latDegreeToWVPressureMbarAmpMap[INDEX_75_DEGREES] * amplitudeScaleFactor;
      beta =
          latDegreeToBetaAvgMapKPM[INDEX_75_DEGREES]
              - latDegreeToBetaAmpMapKPM[INDEX_75_DEGREES] * amplitudeScaleFactor;
      lambda =
          latDegreeToLambdaAmpMap[INDEX_75_DEGREES]
              - latDegreeToLambdaAmpMap[INDEX_75_DEGREES] * amplitudeScaleFactor;
    }

    double zenithDryDelayAtSeaLevelSeconds = (1.0e-6 * K1 * RD * pressureMbar) / GM;
    double zenithWetDelayAtSeaLevelSeconds =
        (((1.0e-6 * K2 * RD) / (GM * (lambda + 1.0) - beta * RD))
            * (waterVaporPressureMbar / tempKelvin));
    double commonBase = 1.0 - ((beta * heightMetersAboveSeaLevel) / tempKelvin);

    double powerDry = (GRAVITY_MPS2 / (RD * beta));
    double powerWet = (((lambda + 1.0) * GRAVITY_MPS2) / (RD * beta)) - 1.0;
    double zenithDryDelaySeconds = zenithDryDelayAtSeaLevelSeconds * Math.pow(commonBase, powerDry);
    double zenithWetDelaySeconds = zenithWetDelayAtSeaLevelSeconds * Math.pow(commonBase, powerWet);
    return new DryAndWetZenithDelays(zenithDryDelaySeconds, zenithWetDelaySeconds);
  }

  /**
   * Interpolates linearly given two points (point1X, point1Y) and (point2X, point2Y). Given the
   * desired value of x (xInterpolated), an interpolated value of y shall be computed and returned.
   */
  private static double interpolate(
      double point1X, double point1Y, double point2X, double point2Y, double xOutput) {
    // Check that xOutput is between the two interpolation points.
    if ((point1X < point2X && (xOutput < point1X || xOutput > point2X))
        || (point2X < point1X && (xOutput < point2X || xOutput > point1X))) {
      throw new IllegalArgumentException("Interpolated value is outside the interpolated region");
    }
    double deltaX = point2X - point1X;
    double yOutput;

    if (Math.abs(deltaX) > MINIMUM_INTERPOLATION_THRESHOLD) {
      yOutput = point1Y + (xOutput - point1X) / deltaX * (point2Y - point1Y);
    } else {
      yOutput = point1Y;
    }
    return yOutput;
  }

  /** A class containing dry and wet mapping values */
  private static class DryAndWetMappingValues {
    public double dryMappingValue;
    public double wetMappingValue;

    public DryAndWetMappingValues(double dryMappingValue, double wetMappingValue) {
      this.dryMappingValue = dryMappingValue;
      this.wetMappingValue = wetMappingValue;
    }
  }

  /** A class containing dry and wet delays in seconds experienced at zenith */
  private static class DryAndWetZenithDelays {
    public double dryZenithDelaySec;
    public double wetZenithDelaySec;

    public DryAndWetZenithDelays(double dryZenithDelay, double wetZenithDelay) {
      this.dryZenithDelaySec = dryZenithDelay;
      this.wetZenithDelaySec = wetZenithDelay;
    }
  }
}

```

`pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/UserPositionVelocityWeightedLeastSquare.java`:

```java
/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.location.lbs.gnss.gps.pseudorange;

import android.location.cts.nano.Ephemeris.GpsEphemerisProto;
import android.location.cts.nano.Ephemeris.GpsNavMessageProto;
import com.google.common.annotations.VisibleForTesting;
import com.google.common.base.Preconditions;
import com.google.common.collect.Lists;
import com.google.location.lbs.gnss.gps.pseudorange.Ecef2LlaConverter.GeodeticLlaValues;
import com.google.location.lbs.gnss.gps.pseudorange.EcefToTopocentricConverter.TopocentricAEDValues;
import com.google.location.lbs.gnss.gps.pseudorange.SatellitePositionCalculator.PositionAndVelocity;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.LUDecomposition;
import org.apache.commons.math3.linear.QRDecomposition;
import org.apache.commons.math3.linear.RealMatrix;

/**
 * Computes an iterative least square receiver position solution given the pseudorange (meters) and
 * accumulated delta range (meters) measurements, receiver time of week, week number and the
 * navigation message.
 */
class UserPositionVelocityWeightedLeastSquare {
  private static final double SPEED_OF_LIGHT_MPS = 299792458.0;
  private static final int SECONDS_IN_WEEK = 604800;
  private static final double LEAST_SQUARE_TOLERANCE_METERS = 4.0e-8;
  /** Position correction threshold below which atmospheric correction will be applied */
  private static final double ATMOSPHERIC_CORRECTIONS_THRESHOLD_METERS = 1000.0;

  private static final int MINIMUM_NUMBER_OF_SATELLITES = 4;
  private static final double RESIDUAL_TO_REPEAT_LEAST_SQUARE_METERS = 20.0;
  private static final int MAXIMUM_NUMBER_OF_LEAST_SQUARE_ITERATIONS = 100;
  /** GPS C/A code chip width Tc = 1 microseconds */
  private static final double GPS_CHIP_WIDTH_T_C_SEC = 1.0e-6;
  /** Narrow correlator with spacing d = 0.1 chip */
  private static final double GPS_CORRELATOR_SPACING_IN_CHIPS = 0.1;
  /** Average time of DLL correlator T of 20 milliseconds */
  private static final double GPS_DLL_AVERAGING_TIME_SEC = 20.0e-3;
  /** Average signal travel time from GPS satellite and earth */
  private static final double AVERAGE_TRAVEL_TIME_SECONDS = 70.0e-3;

  private static final double SECONDS_PER_NANO = 1.0e-9;
  private static final double DOUBLE_ROUND_OFF_TOLERANCE = 0.0000000001;

  private final PseudorangeSmoother pseudorangeSmoother;
  private double geoidHeightMeters;
  private ElevationApiHelper elevationApiHelper;
  private boolean calculateGeoidMeters = true;
  private RealMatrix geometryMatrix;
  private double[] truthLocationForCorrectedResidualComputationEcef = null;

  /** Constructor */
  public UserPositionVelocityWeightedLeastSquare(PseudorangeSmoother pseudorangeSmoother) {
    this.pseudorangeSmoother = pseudorangeSmoother;
  }

  /** Constructor with Google Elevation API Key */
  public UserPositionVelocityWeightedLeastSquare(
      PseudorangeSmoother pseudorangeSmoother, String elevationApiKey) {
    this.pseudorangeSmoother = pseudorangeSmoother;
    this.elevationApiHelper = new ElevationApiHelper(elevationApiKey);
  }

  /**
   * Sets the reference ground truth for pseudorange residual correction calculation. If no ground
   * truth is set, no corrected pseudorange residual will be calculated.
   */
  public void setTruthLocationForCorrectedResidualComputationEcef(
      double[] groundTruthForResidualCorrectionEcef) {
    this.truthLocationForCorrectedResidualComputationEcef = groundTruthForResidualCorrectionEcef;
  }

  /**
   * Least square solution to calculate the user position given the navigation message, pseudorange
   * and accumulated delta range measurements. Also calculates user velocity non-iteratively from
   * Least square position solution.
   *
   * <p>The method fills the user position and velocity in ECEF coordinates and receiver clock
   * offset in meters and clock offset rate in meters per second.
   *
   * <p>One can choose between no smoothing, using the carrier phase measurements (accumulated delta
   * range) or the doppler measurements (pseudorange rate) for smoothing the pseudorange. The
   * smoothing is applied only if time has changed below a specific threshold since last invocation.
   *
   * <p>Source for least squares:
   *
   * <ul>
   *   <li>http://www.u-blox.com/images/downloads/Product_Docs/GPS_Compendium%28GPS-X-02007%29.pdf
   *       page 81 - 85
   *   <li>Parkinson, B.W., Spilker Jr., J.J.: ‘Global positioning system: theory and applications’
   *       page 412 - 414
   * </ul>
   *
   * <p>Sources for smoothing pseudorange with carrier phase measurements:
   *
   * <ul>
   *   <li>Satellite Communications and Navigation Systems book, page 424,
   *   <li>Principles of GNSS, Inertial, and Multisensor Integrated Navigation Systems, page 388,
   *       389.
   * </ul>
   *
   * <p>The function does not modify the smoothed measurement list {@code
   * immutableSmoothedSatellitesToReceiverMeasurements}
   *
   * @param navMessageProto parameters of the navigation message
   * @param usefulSatellitesToReceiverMeasurements Map of useful satellite PRN to {@link
   *     GpsMeasurementWithRangeAndUncertainty} containing receiver measurements for computing the
   *     position solution.
   * @param receiverGPSTowAtReceptionSeconds Receiver estimate of GPS time of week (seconds)
   * @param receiverGPSWeek Receiver estimate of GPS week (0-1024+)
   * @param dayOfYear1To366 The day of the year between 1 and 366
   * @param positionVelocitySolutionECEF Solution array of the following format: [0-2] xyz solution
   *     of user. [3] clock bias of user. [4-6] velocity of user. [7] clock bias rate of user.
   * @param positionVelocityUncertaintyEnu Uncertainty of calculated position and velocity solution
   *     in meters and mps local ENU system. Array has the following format: [0-2] Enu uncertainty
   *     of position solution in meters [3-5] Enu uncertainty of velocity solution in meters per
   *     second.
   * @param pseudorangeResidualMeters The pseudorange residual corrected by subtracting expected
   *     pseudorange calculated with the use clock bias of the highest elevation satellites.
   */
  public void calculateUserPositionVelocityLeastSquare(
      GpsNavMessageProto navMessageProto,
      List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToReceiverMeasurements,
      double receiverGPSTowAtReceptionSeconds,
      int receiverGPSWeek,
      int dayOfYear1To366,
      double[] positionVelocitySolutionECEF,
      double[] positionVelocityUncertaintyEnu,
      double[] pseudorangeResidualMeters)
      throws Exception {

    // Use PseudorangeSmoother to smooth the pseudorange according to: Satellite Communications and
    // Navigation Systems book, page 424 and Principles of GNSS, Inertial, and Multisensor
    // Integrated Navigation Systems, page 388, 389.
    double[] deltaPositionMeters;
    List<GpsMeasurementWithRangeAndUncertainty> immutableSmoothedSatellitesToReceiverMeasurements =
        pseudorangeSmoother.updatePseudorangeSmoothingResult(
            Collections.unmodifiableList(usefulSatellitesToReceiverMeasurements));
    List<GpsMeasurementWithRangeAndUncertainty> mutableSmoothedSatellitesToReceiverMeasurements =
        Lists.newArrayList(immutableSmoothedSatellitesToReceiverMeasurements);
    int numberOfUsefulSatellites =
        getNumberOfUsefulSatellites(mutableSmoothedSatellitesToReceiverMeasurements);
    // Least square position solution is supported only if 4 or more satellites visible
    Preconditions.checkArgument(
        numberOfUsefulSatellites >= MINIMUM_NUMBER_OF_SATELLITES,
        "At least 4 satellites have to be visible... Only 3D mode is supported...");
    boolean repeatLeastSquare = false;
    SatellitesPositionPseudorangesResidualAndCovarianceMatrix satPosPseudorangeResidualAndWeight;

    boolean isFirstWLS = true;

    do {
      // Calculate satellites' positions, measurement residuals per visible satellite and
      // weight matrix for the iterative least square
      boolean doAtmosphericCorrections = false;
      satPosPseudorangeResidualAndWeight =
          calculateSatPosAndPseudorangeResidual(
              navMessageProto,
              mutableSmoothedSatellitesToReceiverMeasurements,
              receiverGPSTowAtReceptionSeconds,
              receiverGPSWeek,
              dayOfYear1To366,
              positionVelocitySolutionECEF,
              doAtmosphericCorrections);

      // Calculate the geometry matrix according to "Global Positioning System: Theory and
      // Applications", Parkinson and Spilker page 413
      RealMatrix covarianceMatrixM2 =
          new Array2DRowRealMatrix(satPosPseudorangeResidualAndWeight.covarianceMatrixMetersSquare);
      geometryMatrix =
          new Array2DRowRealMatrix(
              calculateGeometryMatrix(
                  satPosPseudorangeResidualAndWeight.satellitesPositionsMeters,
                  positionVelocitySolutionECEF));
      RealMatrix weightedGeometryMatrix;
      RealMatrix weightMatrixMetersMinus2 = null;
      // Apply weighted least square only if the covariance matrix is not singular (has a non-zero
      // determinant), otherwise apply ordinary least square. The reason is to ignore reported
      // signal to noise ratios by the receiver that can lead to such singularities
      LUDecomposition ludCovMatrixM2 = new LUDecomposition(covarianceMatrixM2);
      double det = ludCovMatrixM2.getDeterminant();

      if (det <= DOUBLE_ROUND_OFF_TOLERANCE) {
        // Do not weight the geometry matrix if covariance matrix is singular.
        weightedGeometryMatrix = geometryMatrix;
      } else {
        weightMatrixMetersMinus2 = ludCovMatrixM2.getSolver().getInverse();
        RealMatrix hMatrix = calculateHMatrix(weightMatrixMetersMinus2, geometryMatrix);
        weightedGeometryMatrix =
            hMatrix.multiply(geometryMatrix.transpose()).multiply(weightMatrixMetersMinus2);
      }

      // Equation 9 page 413 from "Global Positioning System: Theory and Applications", Parkinson
      // and Spilker
      deltaPositionMeters =
          GpsMathOperations.matrixByColVectMultiplication(
              weightedGeometryMatrix.getData(),
              satPosPseudorangeResidualAndWeight.pseudorangeResidualsMeters);

      // Apply corrections to the position estimate
      positionVelocitySolutionECEF[0] += deltaPositionMeters[0];
      positionVelocitySolutionECEF[1] += deltaPositionMeters[1];
      positionVelocitySolutionECEF[2] += deltaPositionMeters[2];
      positionVelocitySolutionECEF[3] += deltaPositionMeters[3];
      // Iterate applying corrections to the position solution until correction is below threshold
      satPosPseudorangeResidualAndWeight =
          applyWeightedLeastSquare(
              navMessageProto,
              mutableSmoothedSatellitesToReceiverMeasurements,
              receiverGPSTowAtReceptionSeconds,
              receiverGPSWeek,
              dayOfYear1To366,
              positionVelocitySolutionECEF,
              deltaPositionMeters,
              doAtmosphericCorrections,
              satPosPseudorangeResidualAndWeight,
              weightMatrixMetersMinus2);

      // We use the first WLS iteration results and correct them based on the ground truth position
      // and using a clock error computed from high elevation satellites. The first iteration is
      // used before satellite with high residuals being removed.
      if (isFirstWLS && truthLocationForCorrectedResidualComputationEcef != null) {
        // Snapshot the information needed before high residual satellites are removed
        System.arraycopy(
            ResidualCorrectionCalculator.calculateCorrectedResiduals(
                satPosPseudorangeResidualAndWeight,
                positionVelocitySolutionECEF.clone(),
                truthLocationForCorrectedResidualComputationEcef),
            0 /*source starting pos*/,
            pseudorangeResidualMeters,
            0 /*destination starting pos*/,
            GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES /*length of elements*/);
        isFirstWLS = false;
      }
      repeatLeastSquare = false;
      int satsWithResidualBelowThreshold =
          satPosPseudorangeResidualAndWeight.pseudorangeResidualsMeters.length;
      // remove satellites that have residuals above RESIDUAL_TO_REPEAT_LEAST_SQUARE_METERS as they
      // worsen the position solution accuracy. If any satellite is removed, repeat the least square
      repeatLeastSquare =
          removeHighResidualSats(
              mutableSmoothedSatellitesToReceiverMeasurements,
              repeatLeastSquare,
              satPosPseudorangeResidualAndWeight,
              satsWithResidualBelowThreshold);

    } while (repeatLeastSquare);
    calculateGeoidMeters = false;

    // The computed ECEF position will be used next to compute the user velocity.
    // we calculate and fill in the user velocity solutions based on following equation:
    // Weight Matrix * GeometryMatrix * User Velocity Vector
    // = Weight Matrix * deltaPseudoRangeRateWeightedMps
    // Reference: Pratap Misra and Per Enge
    // "Global Positioning System: Signals, Measurements, and Performance" Page 218.

    // Get the number of satellite used in Geometry Matrix
    numberOfUsefulSatellites = geometryMatrix.getRowDimension();

    RealMatrix rangeRateMps = new Array2DRowRealMatrix(numberOfUsefulSatellites, 1);
    RealMatrix deltaPseudoRangeRateMps = new Array2DRowRealMatrix(numberOfUsefulSatellites, 1);
    RealMatrix pseudorangeRateWeight =
        new Array2DRowRealMatrix(numberOfUsefulSatellites, numberOfUsefulSatellites);

    // Correct the receiver time of week with the estimated receiver clock bias
    receiverGPSTowAtReceptionSeconds =
        receiverGPSTowAtReceptionSeconds - positionVelocitySolutionECEF[3] / SPEED_OF_LIGHT_MPS;

    int measurementCount = 0;

    // Calculate range rates
    for (int i = 0; i < GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES; i++) {
      if (mutableSmoothedSatellitesToReceiverMeasurements.get(i) != null) {
        GpsEphemerisProto ephemeridesProto = getEphemerisForSatellite(navMessageProto, i + 1);

        double pseudorangeMeasurementMeters =
            mutableSmoothedSatellitesToReceiverMeasurements.get(i).pseudorangeMeters;
        GpsTimeOfWeekAndWeekNumber correctedTowAndWeek =
            calculateCorrectedTransmitTowAndWeek(
                ephemeridesProto,
                receiverGPSTowAtReceptionSeconds,
                receiverGPSWeek,
                pseudorangeMeasurementMeters);

        // Calculate satellite velocity
        PositionAndVelocity satPosECEFMetersVelocityMPS =
            SatellitePositionCalculator.calculateSatellitePositionAndVelocityFromEphemeris(
                ephemeridesProto,
                correctedTowAndWeek.gpsTimeOfWeekSeconds,
                correctedTowAndWeek.weekNumber,
                positionVelocitySolutionECEF[0],
                positionVelocitySolutionECEF[1],
                positionVelocitySolutionECEF[2]);

        // Calculate satellite clock error rate
        double satelliteClockErrorRateMps =
            SatelliteClockCorrectionCalculator.calculateSatClockCorrErrorRate(
                ephemeridesProto,
                correctedTowAndWeek.gpsTimeOfWeekSeconds,
                correctedTowAndWeek.weekNumber);

        // Fill in range rates. range rate = satellite velocity (dot product) line-of-sight vector
        rangeRateMps.setEntry(
            measurementCount,
            0,
            -1
                * (satPosECEFMetersVelocityMPS.velocityXMetersPerSec
                        * geometryMatrix.getEntry(measurementCount, 0)
                    + satPosECEFMetersVelocityMPS.velocityYMetersPerSec
                        * geometryMatrix.getEntry(measurementCount, 1)
                    + satPosECEFMetersVelocityMPS.velocityZMetersPerSec
                        * geometryMatrix.getEntry(measurementCount, 2)));

        deltaPseudoRangeRateMps.setEntry(
            measurementCount,
            0,
            mutableSmoothedSatellitesToReceiverMeasurements.get(i).pseudorangeRateMps
                - rangeRateMps.getEntry(measurementCount, 0)
                + satelliteClockErrorRateMps
                - positionVelocitySolutionECEF[7]);

        // Calculate the velocity weight matrix by using 1 / square(PseudorangeRate Uncertainty)
        // along the diagonal
        pseudorangeRateWeight.setEntry(
            measurementCount,
            measurementCount,
            1
                / (mutableSmoothedSatellitesToReceiverMeasurements.get(i)
                        .pseudorangeRateUncertaintyMps
                    * mutableSmoothedSatellitesToReceiverMeasurements.get(i)
                        .pseudorangeRateUncertaintyMps));
        measurementCount++;
      }
    }

    RealMatrix weightedGeoMatrix = pseudorangeRateWeight.multiply(geometryMatrix);
    RealMatrix deltaPseudoRangeRateWeightedMps =
        pseudorangeRateWeight.multiply(deltaPseudoRangeRateMps);
    QRDecomposition qrdWeightedGeoMatrix = new QRDecomposition(weightedGeoMatrix);
    RealMatrix velocityMps =
        qrdWeightedGeoMatrix.getSolver().solve(deltaPseudoRangeRateWeightedMps);
    positionVelocitySolutionECEF[4] = velocityMps.getEntry(0, 0);
    positionVelocitySolutionECEF[5] = velocityMps.getEntry(1, 0);
    positionVelocitySolutionECEF[6] = velocityMps.getEntry(2, 0);
    positionVelocitySolutionECEF[7] = velocityMps.getEntry(3, 0);

    RealMatrix pseudorangeWeight =
        new LUDecomposition(
                new Array2DRowRealMatrix(
                    satPosPseudorangeResidualAndWeight.covarianceMatrixMetersSquare))
            .getSolver()
            .getInverse();

    // Calculate and store the uncertainties of position and velocity in local ENU system in meters
    // and meters per second.
    double[] pvUncertainty =
        calculatePositionVelocityUncertaintyEnu(
            pseudorangeRateWeight, pseudorangeWeight, positionVelocitySolutionECEF);
    System.arraycopy(
        pvUncertainty,
        0 /*source starting pos*/,
        positionVelocityUncertaintyEnu,
        0 /*destination starting pos*/,
        6 /*length of elements*/);
  }

  /**
   * Calculates the position uncertainty in meters and the velocity uncertainty in meters per second
   * solution in local ENU system.
   *
   * <p>Reference: Global Positioning System: Signals, Measurements, and Performance by Pratap
   * Misra, Per Enge, Page 206 - 209.
   *
   * @param velocityWeightMatrix the velocity weight matrix
   * @param positionWeightMatrix the position weight matrix
   * @param positionVelocitySolution the position and velocity solution in ECEF
   * @return an array containing the position and velocity uncertainties in ENU coordinate system.
   *     [0-2] Enu uncertainty of position solution in meters. [3-5] Enu uncertainty of velocity
   *     solution in meters per second.
   */
  public double[] calculatePositionVelocityUncertaintyEnu(
      RealMatrix velocityWeightMatrix,
      RealMatrix positionWeightMatrix,
      double[] positionVelocitySolution) {

    if (geometryMatrix == null) {
      return null;
    }

    RealMatrix velocityH = calculateHMatrix(velocityWeightMatrix, geometryMatrix);
    RealMatrix positionH = calculateHMatrix(positionWeightMatrix, geometryMatrix);

    // Calculate the rotation Matrix to convert to local ENU system.
    RealMatrix rotationMatrix = new Array2DRowRealMatrix(4, 4);
    GeodeticLlaValues llaValues =
        Ecef2LlaConverter.convertECEFToLLACloseForm(
            positionVelocitySolution[0], positionVelocitySolution[1], positionVelocitySolution[2]);
    rotationMatrix.setSubMatrix(
        Ecef2EnuConverter.getRotationMatrix(llaValues.longitudeRadians, llaValues.latitudeRadians)
            .getData(),
        0,
        0);
    rotationMatrix.setEntry(3, 3, 1);

    // Convert to local ENU by pre-multiply rotation matrix and multiply rotation matrix transposed
    velocityH = rotationMatrix.multiply(velocityH).multiply(rotationMatrix.transpose());
    positionH = rotationMatrix.multiply(positionH).multiply(rotationMatrix.transpose());

    // Return the square root of diagonal entries
    return new double[] {
      Math.sqrt(positionH.getEntry(0, 0)), Math.sqrt(positionH.getEntry(1, 1)),
      Math.sqrt(positionH.getEntry(2, 2)), Math.sqrt(velocityH.getEntry(0, 0)),
      Math.sqrt(velocityH.getEntry(1, 1)), Math.sqrt(velocityH.getEntry(2, 2))
    };
  }

  /**
   * Calculates the measurement connection matrix H as a function of weightMatrix and
   * geometryMatrix.
   *
   * <p>H = (geometryMatrixTransposed * Weight * geometryMatrix) ^ -1
   *
   * <p>Reference: Global Positioning System: Signals, Measurements, and Performance, P207
   *
   * @param weightMatrix Weights for computing H Matrix
   * @return H Matrix
   */
  private RealMatrix calculateHMatrix(RealMatrix weightMatrix, RealMatrix geometryMatrix) {

    RealMatrix tempH = geometryMatrix.transpose().multiply(weightMatrix).multiply(geometryMatrix);
    return new LUDecomposition(tempH).getSolver().getInverse();
  }

  /**
   * Applies weighted least square iterations and corrects to the position solution until correction
   * is below threshold. An exception is thrown if the maximum number of iterations: {@value
   * #MAXIMUM_NUMBER_OF_LEAST_SQUARE_ITERATIONS} is reached without convergence.
   */
  private SatellitesPositionPseudorangesResidualAndCovarianceMatrix applyWeightedLeastSquare(
      GpsNavMessageProto navMessageProto,
      List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToReceiverMeasurements,
      double receiverGPSTowAtReceptionSeconds,
      int receiverGPSWeek,
      int dayOfYear1To366,
      double[] positionSolutionECEF,
      double[] deltaPositionMeters,
      boolean doAtmosphericCorrections,
      SatellitesPositionPseudorangesResidualAndCovarianceMatrix satPosPseudorangeResidualAndWeight,
      RealMatrix weightMatrixMetersMinus2)
      throws Exception {
    RealMatrix weightedGeometryMatrix;
    int numberOfIterations = 0;

    while ((Math.abs(deltaPositionMeters[0])
            + Math.abs(deltaPositionMeters[1])
            + Math.abs(deltaPositionMeters[2]))
        >= LEAST_SQUARE_TOLERANCE_METERS) {
      // Apply ionospheric and tropospheric corrections only if the applied correction to
      // position is below a specific threshold
      if ((Math.abs(deltaPositionMeters[0])
              + Math.abs(deltaPositionMeters[1])
              + Math.abs(deltaPositionMeters[2]))
          < ATMOSPHERIC_CORRECTIONS_THRESHOLD_METERS) {
        doAtmosphericCorrections = true;
      }
      // Calculate satellites' positions, measurement residual per visible satellite and
      // weight matrix for the iterative least square
      satPosPseudorangeResidualAndWeight =
          calculateSatPosAndPseudorangeResidual(
              navMessageProto,
              usefulSatellitesToReceiverMeasurements,
              receiverGPSTowAtReceptionSeconds,
              receiverGPSWeek,
              dayOfYear1To366,
              positionSolutionECEF,
              doAtmosphericCorrections);

      // Calculate the geometry matrix according to "Global Positioning System: Theory and
      // Applications", Parkinson and Spilker page 413
      geometryMatrix =
          new Array2DRowRealMatrix(
              calculateGeometryMatrix(
                  satPosPseudorangeResidualAndWeight.satellitesPositionsMeters,
                  positionSolutionECEF));
      // Apply weighted least square only if the covariance matrix is
      // not singular (has a non-zero determinant), otherwise apply ordinary least square.
      // The reason is to ignore reported signal to noise ratios by the receiver that can
      // lead to such singularities
      if (weightMatrixMetersMinus2 == null) {
        weightedGeometryMatrix = geometryMatrix;
      } else {
        RealMatrix hMatrix = calculateHMatrix(weightMatrixMetersMinus2, geometryMatrix);
        weightedGeometryMatrix =
            hMatrix.multiply(geometryMatrix.transpose()).multiply(weightMatrixMetersMinus2);
      }

      // Equation 9 page 413 from "Global Positioning System: Theory and Applications",
      // Parkinson and Spilker
      deltaPositionMeters =
          GpsMathOperations.matrixByColVectMultiplication(
              weightedGeometryMatrix.getData(),
              satPosPseudorangeResidualAndWeight.pseudorangeResidualsMeters);

      // Apply corrections to the position estimate
      positionSolutionECEF[0] += deltaPositionMeters[0];
      positionSolutionECEF[1] += deltaPositionMeters[1];
      positionSolutionECEF[2] += deltaPositionMeters[2];
      positionSolutionECEF[3] += deltaPositionMeters[3];
      numberOfIterations++;
      Preconditions.checkArgument(
          numberOfIterations <= MAXIMUM_NUMBER_OF_LEAST_SQUARE_ITERATIONS,
          "Maximum number of least square iterations reached without convergence...");
    }
    return satPosPseudorangeResidualAndWeight;
  }

  /**
   * Removes satellites that have residuals above {@value #RESIDUAL_TO_REPEAT_LEAST_SQUARE_METERS}
   * from the {@code usefulSatellitesToReceiverMeasurements} list. Returns true if any satellite is
   * removed.
   */
  private boolean removeHighResidualSats(
      List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToReceiverMeasurements,
      boolean repeatLeastSquare,
      SatellitesPositionPseudorangesResidualAndCovarianceMatrix satPosPseudorangeResidualAndWeight,
      int satsWithResidualBelowThreshold) {

    for (int i = 0; i < satPosPseudorangeResidualAndWeight.pseudorangeResidualsMeters.length; i++) {
      if (satsWithResidualBelowThreshold > MINIMUM_NUMBER_OF_SATELLITES) {
        if (Math.abs(satPosPseudorangeResidualAndWeight.pseudorangeResidualsMeters[i])
            > RESIDUAL_TO_REPEAT_LEAST_SQUARE_METERS) {
          int prn = satPosPseudorangeResidualAndWeight.satellitePRNs[i];
          usefulSatellitesToReceiverMeasurements.set(prn - 1, null);
          satsWithResidualBelowThreshold--;
          repeatLeastSquare = true;
        }
      }
    }
    return repeatLeastSquare;
  }

  /**
   * Calculates position of all visible satellites and pseudorange measurement residual (difference
   * of measured to predicted pseudoranges) needed for the least square computation. The result is
   * stored in an instance of {@link SatellitesPositionPseudorangesResidualAndCovarianceMatrix}
   *
   * @param navMessageProto parameters of the navigation message
   * @param usefulSatellitesToReceiverMeasurements Map of useful satellite PRN to {@link
   *     GpsMeasurementWithRangeAndUncertainty} containing receiver measurements for computing the
   *     position solution
   * @param receiverGPSTowAtReceptionSeconds Receiver estimate of GPS time of week (seconds)
   * @param receiverGpsWeek Receiver estimate of GPS week (0-1024+)
   * @param dayOfYear1To366 The day of the year between 1 and 366
   * @param userPositionECEFMeters receiver ECEF position in meters
   * @param doAtmosphericCorrections boolean indicating if atmospheric range corrections should be
   *     applied
   * @return SatellitesPositionPseudorangesResidualAndCovarianceMatrix Object containing satellite
   *     prns, satellite positions in ECEF, pseudorange residuals and covariance matrix.
   */
  public SatellitesPositionPseudorangesResidualAndCovarianceMatrix
      calculateSatPosAndPseudorangeResidual(
          GpsNavMessageProto navMessageProto,
          List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToReceiverMeasurements,
          double receiverGPSTowAtReceptionSeconds,
          int receiverGpsWeek,
          int dayOfYear1To366,
          double[] userPositionECEFMeters,
          boolean doAtmosphericCorrections)
          throws Exception {
    int numberOfUsefulSatellites =
        getNumberOfUsefulSatellites(usefulSatellitesToReceiverMeasurements);
    // deltaPseudorange is the pseudorange measurement residual
    double[] deltaPseudorangesMeters = new double[numberOfUsefulSatellites];
    double[][] satellitesPositionsECEFMeters = new double[numberOfUsefulSatellites][3];

    // satellite PRNs
    int[] satellitePRNs = new int[numberOfUsefulSatellites];

    // Ionospheric model parameters
    double[] alpha = {
      navMessageProto.iono.alpha[0],
      navMessageProto.iono.alpha[1],
      navMessageProto.iono.alpha[2],
      navMessageProto.iono.alpha[3]
    };
    double[] beta = {
      navMessageProto.iono.beta[0],
      navMessageProto.iono.beta[1],
      navMessageProto.iono.beta[2],
      navMessageProto.iono.beta[3]
    };
    // Weight matrix for the weighted least square
    RealMatrix covarianceMatrixMetersSquare =
        new Array2DRowRealMatrix(numberOfUsefulSatellites, numberOfUsefulSatellites);
    calculateSatPosAndResiduals(
        navMessageProto,
        usefulSatellitesToReceiverMeasurements,
        receiverGPSTowAtReceptionSeconds,
        receiverGpsWeek,
        dayOfYear1To366,
        userPositionECEFMeters,
        doAtmosphericCorrections,
        deltaPseudorangesMeters,
        satellitesPositionsECEFMeters,
        satellitePRNs,
        alpha,
        beta,
        covarianceMatrixMetersSquare);

    return new SatellitesPositionPseudorangesResidualAndCovarianceMatrix(
        satellitePRNs,
        satellitesPositionsECEFMeters,
        deltaPseudorangesMeters,
        covarianceMatrixMetersSquare.getData());
  }

  /**
   * Calculates and fill the position of all visible satellites: {@code
   * satellitesPositionsECEFMeters}, pseudorange measurement residual (difference of measured to
   * predicted pseudoranges): {@code deltaPseudorangesMeters} and covariance matrix from the
   * weighted least square: {@code covarianceMatrixMetersSquare}. An array of the satellite PRNs
   * {@code satellitePRNs} is as well filled.
   */
  private void calculateSatPosAndResiduals(
      GpsNavMessageProto navMessageProto,
      List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToReceiverMeasurements,
      double receiverGPSTowAtReceptionSeconds,
      int receiverGpsWeek,
      int dayOfYear1To366,
      double[] userPositionECEFMeters,
      boolean doAtmosphericCorrections,
      double[] deltaPseudorangesMeters,
      double[][] satellitesPositionsECEFMeters,
      int[] satellitePRNs,
      double[] alpha,
      double[] beta,
      RealMatrix covarianceMatrixMetersSquare)
      throws Exception {
    // user position without the clock estimate
    double[] userPositionTempECEFMeters = {
      userPositionECEFMeters[0], userPositionECEFMeters[1], userPositionECEFMeters[2]
    };
    int satsCounter = 0;
    for (int i = 0; i < GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES; i++) {
      if (usefulSatellitesToReceiverMeasurements.get(i) != null) {
        GpsEphemerisProto ephemeridesProto = getEphemerisForSatellite(navMessageProto, i + 1);
        // Correct the receiver time of week with the estimated receiver clock bias
        receiverGPSTowAtReceptionSeconds =
            receiverGPSTowAtReceptionSeconds - userPositionECEFMeters[3] / SPEED_OF_LIGHT_MPS;

        double pseudorangeMeasurementMeters =
            usefulSatellitesToReceiverMeasurements.get(i).pseudorangeMeters;
        double pseudorangeUncertaintyMeters =
            usefulSatellitesToReceiverMeasurements.get(i).pseudorangeUncertaintyMeters;

        // Assuming uncorrelated pseudorange measurements, the covariance matrix will be diagonal as
        // follows
        covarianceMatrixMetersSquare.setEntry(
            satsCounter, satsCounter, pseudorangeUncertaintyMeters * pseudorangeUncertaintyMeters);

        // Calculate time of week at transmission time corrected with the satellite clock drift
        GpsTimeOfWeekAndWeekNumber correctedTowAndWeek =
            calculateCorrectedTransmitTowAndWeek(
                ephemeridesProto,
                receiverGPSTowAtReceptionSeconds,
                receiverGpsWeek,
                pseudorangeMeasurementMeters);

        // calculate satellite position and velocity
        PositionAndVelocity satPosECEFMetersVelocityMPS =
            SatellitePositionCalculator.calculateSatellitePositionAndVelocityFromEphemeris(
                ephemeridesProto,
                correctedTowAndWeek.gpsTimeOfWeekSeconds,
                correctedTowAndWeek.weekNumber,
                userPositionECEFMeters[0],
                userPositionECEFMeters[1],
                userPositionECEFMeters[2]);

        satellitesPositionsECEFMeters[satsCounter][0] = satPosECEFMetersVelocityMPS.positionXMeters;
        satellitesPositionsECEFMeters[satsCounter][1] = satPosECEFMetersVelocityMPS.positionYMeters;
        satellitesPositionsECEFMeters[satsCounter][2] = satPosECEFMetersVelocityMPS.positionZMeters;

        // Calculate ionospheric and tropospheric corrections
        double ionosphericCorrectionMeters;
        double troposphericCorrectionMeters;
        if (doAtmosphericCorrections) {
          ionosphericCorrectionMeters =
              IonosphericModel.ionoKlobucharCorrectionSeconds(
                      userPositionTempECEFMeters,
                      satellitesPositionsECEFMeters[satsCounter],
                      correctedTowAndWeek.gpsTimeOfWeekSeconds,
                      alpha,
                      beta,
                      IonosphericModel.L1_FREQ_HZ)
                  * SPEED_OF_LIGHT_MPS;

          troposphericCorrectionMeters =
              calculateTroposphericCorrectionMeters(
                  dayOfYear1To366,
                  satellitesPositionsECEFMeters,
                  userPositionTempECEFMeters,
                  satsCounter);
        } else {
          troposphericCorrectionMeters = 0.0;
          ionosphericCorrectionMeters = 0.0;
        }
        double predictedPseudorangeMeters =
            calculatePredictedPseudorange(
                userPositionECEFMeters,
                satellitesPositionsECEFMeters,
                userPositionTempECEFMeters,
                satsCounter,
                ephemeridesProto,
                correctedTowAndWeek,
                ionosphericCorrectionMeters,
                troposphericCorrectionMeters);

        // Pseudorange residual (difference of measured to predicted pseudoranges)
        deltaPseudorangesMeters[satsCounter] =
            pseudorangeMeasurementMeters - predictedPseudorangeMeters;

        // Satellite PRNs
        satellitePRNs[satsCounter] = i + 1;
        satsCounter++;
      }
    }
  }

  /** Searches ephemerides list for the ephemeris associated with current satellite in process */
  private GpsEphemerisProto getEphemerisForSatellite(
      GpsNavMessageProto navMessageProto, int satPrn) {
    List<GpsEphemerisProto> ephemeridesList =
        new ArrayList<GpsEphemerisProto>(Arrays.asList(navMessageProto.ephemerids));
    GpsEphemerisProto ephemeridesProto = null;
    int ephemerisPrn = 0;
    for (GpsEphemerisProto ephProtoFromList : ephemeridesList) {
      ephemerisPrn = ephProtoFromList.prn;
      if (ephemerisPrn == satPrn) {
        ephemeridesProto = ephProtoFromList;
        break;
      }
    }
    return ephemeridesProto;
  }

  /** Calculates predicted pseudorange in meters */
  private double calculatePredictedPseudorange(
      double[] userPositionECEFMeters,
      double[][] satellitesPositionsECEFMeters,
      double[] userPositionNoClockECEFMeters,
      int satsCounter,
      GpsEphemerisProto ephemeridesProto,
      GpsTimeOfWeekAndWeekNumber correctedTowAndWeek,
      double ionosphericCorrectionMeters,
      double troposphericCorrectionMeters)
      throws Exception {
    // Calculate the satellite clock drift
    double satelliteClockCorrectionMeters =
        SatelliteClockCorrectionCalculator.calculateSatClockCorrAndEccAnomAndTkIteratively(
                ephemeridesProto,
                correctedTowAndWeek.gpsTimeOfWeekSeconds,
                correctedTowAndWeek.weekNumber)
            .satelliteClockCorrectionMeters;

    double satelliteToUserDistanceMeters =
        GpsMathOperations.vectorNorm(
            GpsMathOperations.subtractTwoVectors(
                satellitesPositionsECEFMeters[satsCounter], userPositionNoClockECEFMeters));
    // Predicted pseudorange
    double predictedPseudorangeMeters =
        satelliteToUserDistanceMeters
            - satelliteClockCorrectionMeters
            + ionosphericCorrectionMeters
            + troposphericCorrectionMeters
            + userPositionECEFMeters[3];
    return predictedPseudorangeMeters;
  }

  /** Calculates the Gps tropospheric correction in meters */
  private double calculateTroposphericCorrectionMeters(
      int dayOfYear1To366,
      double[][] satellitesPositionsECEFMeters,
      double[] userPositionTempECEFMeters,
      int satsCounter) {
    double troposphericCorrectionMeters;
    TopocentricAEDValues elevationAzimuthDist =
        EcefToTopocentricConverter.convertCartesianToTopocentricRadMeters(
            userPositionTempECEFMeters,
            GpsMathOperations.subtractTwoVectors(
                satellitesPositionsECEFMeters[satsCounter], userPositionTempECEFMeters));

    GeodeticLlaValues lla =
        Ecef2LlaConverter.convertECEFToLLACloseForm(
            userPositionTempECEFMeters[0],
            userPositionTempECEFMeters[1],
            userPositionTempECEFMeters[2]);

    // Geoid of the area where the receiver is located is calculated once and used for the
    // rest of the dataset as it change very slowly over wide area. This to save the delay
    // associated with accessing Google Elevation API. We assume this very first iteration of WLS
    // will compute the correct altitude above the ellipsoid of the ground at the latitude and
    // longitude
    if (calculateGeoidMeters) {
      double elevationAboveSeaLevelMeters = 0;
      if (elevationApiHelper == null) {
        System.out.println(
            "No Google API key is set. Elevation above sea level is set to "
                + "default 0 meters. This may cause inaccuracy in tropospheric correction.");
      } else {
        try {
          elevationAboveSeaLevelMeters =
              elevationApiHelper.getElevationAboveSeaLevelMeters(
                  Math.toDegrees(lla.latitudeRadians), Math.toDegrees(lla.longitudeRadians));
        } catch (Exception e) {
          e.printStackTrace();
          System.out.println(
              "Error when getting elevation from Google Server. "
                  + "Could be wrong Api key or network error. Elevation above sea level is set to "
                  + "default 0 meters. This may cause inaccuracy in tropospheric correction.");
        }
      }

      geoidHeightMeters =
          ElevationApiHelper.calculateGeoidHeightMeters(
              lla.altitudeMeters, elevationAboveSeaLevelMeters);
      troposphericCorrectionMeters =
          TroposphericModelEgnos.calculateTropoCorrectionMeters(
              elevationAzimuthDist.elevationRadians,
              lla.latitudeRadians,
              elevationAboveSeaLevelMeters,
              dayOfYear1To366);
    } else {
      troposphericCorrectionMeters =
          TroposphericModelEgnos.calculateTropoCorrectionMeters(
              elevationAzimuthDist.elevationRadians,
              lla.latitudeRadians,
              lla.altitudeMeters - geoidHeightMeters,
              dayOfYear1To366);
    }
    return troposphericCorrectionMeters;
  }

  /**
   * Gets the number of useful satellites from a list of {@link
   * GpsMeasurementWithRangeAndUncertainty}.
   */
  private int getNumberOfUsefulSatellites(
      List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToReceiverMeasurements) {
    // calculate the number of useful satellites
    int numberOfUsefulSatellites = 0;
    for (int i = 0; i < usefulSatellitesToReceiverMeasurements.size(); i++) {
      if (usefulSatellitesToReceiverMeasurements.get(i) != null) {
        numberOfUsefulSatellites++;
      }
    }
    return numberOfUsefulSatellites;
  }

  /**
   * Computes the GPS time of week at the time of transmission and as well the corrected GPS week
   * taking into consideration week rollover. The returned GPS time of week is corrected by the
   * computed satellite clock drift. The result is stored in an instance of {@link
   * GpsTimeOfWeekAndWeekNumber}
   *
   * @param ephemerisProto parameters of the navigation message
   * @param receiverGpsTowAtReceptionSeconds Receiver estimate of GPS time of week when signal was
   *     received (seconds)
   * @param receiverGpsWeek Receiver estimate of GPS week (0-1024+)
   * @param pseudorangeMeters Measured pseudorange in meters
   * @return GpsTimeOfWeekAndWeekNumber Object containing Gps time of week and week number.
   */
  private static GpsTimeOfWeekAndWeekNumber calculateCorrectedTransmitTowAndWeek(
      GpsEphemerisProto ephemerisProto,
      double receiverGpsTowAtReceptionSeconds,
      int receiverGpsWeek,
      double pseudorangeMeters)
      throws Exception {
    // GPS time of week at time of transmission: Gps time corrected for transit time (page 98 ICD
    // GPS 200)
    double receiverGpsTowAtTimeOfTransmission =
        receiverGpsTowAtReceptionSeconds - pseudorangeMeters / SPEED_OF_LIGHT_MPS;

    // Adjust for week rollover
    if (receiverGpsTowAtTimeOfTransmission < 0) {
      receiverGpsTowAtTimeOfTransmission += SECONDS_IN_WEEK;
      receiverGpsWeek -= 1;
    } else if (receiverGpsTowAtTimeOfTransmission > SECONDS_IN_WEEK) {
      receiverGpsTowAtTimeOfTransmission -= SECONDS_IN_WEEK;
      receiverGpsWeek += 1;
    }

    // Compute the satellite clock correction term (Seconds)
    double clockCorrectionSeconds =
        SatelliteClockCorrectionCalculator.calculateSatClockCorrAndEccAnomAndTkIteratively(
                    ephemerisProto, receiverGpsTowAtTimeOfTransmission, receiverGpsWeek)
                .satelliteClockCorrectionMeters
            / SPEED_OF_LIGHT_MPS;

    // Correct with the satellite clock correction term
    double receiverGpsTowAtTimeOfTransmissionCorrectedSec =
        receiverGpsTowAtTimeOfTransmission + clockCorrectionSeconds;

    // Adjust for week rollover due to satellite clock correction
    if (receiverGpsTowAtTimeOfTransmissionCorrectedSec < 0.0) {
      receiverGpsTowAtTimeOfTransmissionCorrectedSec += SECONDS_IN_WEEK;
      receiverGpsWeek -= 1;
    }
    if (receiverGpsTowAtTimeOfTransmissionCorrectedSec > SECONDS_IN_WEEK) {
      receiverGpsTowAtTimeOfTransmissionCorrectedSec -= SECONDS_IN_WEEK;
      receiverGpsWeek += 1;
    }
    return new GpsTimeOfWeekAndWeekNumber(
        receiverGpsTowAtTimeOfTransmissionCorrectedSec, receiverGpsWeek);
  }

  /**
   * Calculates the Geometry matrix (describing user to satellite geometry) given a list of
   * satellite positions in ECEF coordinates in meters and the user position in ECEF in meters.
   *
   * <p>The geometry matrix has four columns, and rows equal to the number of satellites. For each
   * of the rows (i.e. for each of the satellites used), the columns are filled with the normalized
   * line–of-sight vectors and 1 s for the fourth column.
   *
   * <p>Source: Parkinson, B.W., Spilker Jr., J.J.: ‘Global positioning system: theory and
   * applications’ page 413
   */
  private static double[][] calculateGeometryMatrix(
      double[][] satellitePositionsECEFMeters, double[] userPositionECEFMeters) {

    double[][] geometryMatrix = new double[satellitePositionsECEFMeters.length][4];
    for (int i = 0; i < satellitePositionsECEFMeters.length; i++) {
      geometryMatrix[i][3] = 1;
    }
    // iterate over all satellites
    for (int i = 0; i < satellitePositionsECEFMeters.length; i++) {
      double[] r = {
        satellitePositionsECEFMeters[i][0] - userPositionECEFMeters[0],
        satellitePositionsECEFMeters[i][1] - userPositionECEFMeters[1],
        satellitePositionsECEFMeters[i][2] - userPositionECEFMeters[2]
      };
      double norm = Math.sqrt(Math.pow(r[0], 2) + Math.pow(r[1], 2) + Math.pow(r[2], 2));
      for (int j = 0; j < 3; j++) {
        geometryMatrix[i][j] =
            (userPositionECEFMeters[j] - satellitePositionsECEFMeters[i][j]) / norm;
      }
    }
    return geometryMatrix;
  }

  /**
   * Class containing satellites' PRNs, satellites' positions in ECEF meters, the pseudorange
   * residual per visible satellite in meters and the covariance matrix of the pseudoranges in
   * meters square
   */
  protected static class SatellitesPositionPseudorangesResidualAndCovarianceMatrix {

    /** Satellites' PRNs */
    protected final int[] satellitePRNs;

    /** ECEF positions (meters) of useful satellites */
    protected final double[][] satellitesPositionsMeters;

    /** Pseudorange measurement residuals (difference of measured to predicted pseudoranges) */
    protected final double[] pseudorangeResidualsMeters;

    /** Pseudorange covariance Matrix for the weighted least squares (meters square) */
    protected final double[][] covarianceMatrixMetersSquare;

    /** Constructor */
    private SatellitesPositionPseudorangesResidualAndCovarianceMatrix(
        int[] satellitePRNs,
        double[][] satellitesPositionsMeters,
        double[] pseudorangeResidualsMeters,
        double[][] covarianceMatrixMetersSquare) {
      this.satellitePRNs = satellitePRNs;
      this.satellitesPositionsMeters = satellitesPositionsMeters;
      this.pseudorangeResidualsMeters = pseudorangeResidualsMeters;
      this.covarianceMatrixMetersSquare = covarianceMatrixMetersSquare;
    }
  }

  /** Class containing GPS time of week in seconds and GPS week number */
  private static class GpsTimeOfWeekAndWeekNumber {
    /** GPS time of week in seconds */
    private final double gpsTimeOfWeekSeconds;

    /** GPS week number */
    private final int weekNumber;

    /** Constructor */
    private GpsTimeOfWeekAndWeekNumber(double gpsTimeOfWeekSeconds, int weekNumber) {
      this.gpsTimeOfWeekSeconds = gpsTimeOfWeekSeconds;
      this.weekNumber = weekNumber;
    }
  }

  /**
   * Uses the common reception time approach to calculate pseudoranges from the time of week
   * measurements reported by the receiver according to http://cdn.intechopen.com/pdfs-wm/27712.pdf.
   * As well computes the pseudoranges uncertainties for each input satellite
   */
  @VisibleForTesting
  static List<GpsMeasurementWithRangeAndUncertainty> computePseudorangeAndUncertainties(
      List<GpsMeasurement> usefulSatellitesToReceiverMeasurements,
      Long[] usefulSatellitesToTOWNs,
      long largestTowNs) {

    List<GpsMeasurementWithRangeAndUncertainty> usefulSatellitesToPseudorangeMeasurements =
        Arrays.asList(
            new GpsMeasurementWithRangeAndUncertainty
                [GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES]);
    for (int i = 0; i < GpsNavigationMessageStore.MAX_NUMBER_OF_SATELLITES; i++) {
      if (usefulSatellitesToTOWNs[i] != null) {
        double deltai = largestTowNs - usefulSatellitesToTOWNs[i];
        double pseudorangeMeters =
            (AVERAGE_TRAVEL_TIME_SECONDS + deltai * SECONDS_PER_NANO) * SPEED_OF_LIGHT_MPS;

        double signalToNoiseRatioLinear =
            Math.pow(10, usefulSatellitesToReceiverMeasurements.get(i).signalToNoiseRatioDb / 10.0);
        // From Global Positioning System book, Misra and Enge, page 416, the uncertainty of the
        // pseudorange measurement is calculated next.
        // For GPS C/A code chip width Tc = 1 microseconds. Narrow correlator with spacing d = 0.1
        // chip and an average time of DLL correlator T of 20 milliseconds are used.
        double sigmaMeters =
            SPEED_OF_LIGHT_MPS
                * GPS_CHIP_WIDTH_T_C_SEC
                * Math.sqrt(
                    GPS_CORRELATOR_SPACING_IN_CHIPS
                        / (4 * GPS_DLL_AVERAGING_TIME_SEC * signalToNoiseRatioLinear));
        usefulSatellitesToPseudorangeMeasurements.set(
            i,
            new GpsMeasurementWithRangeAndUncertainty(
                usefulSatellitesToReceiverMeasurements.get(i), pseudorangeMeters, sigmaMeters));
      }
    }
    return usefulSatellitesToPseudorangeMeasurements;
  }
}

```

`pseudorange/src/test/java/com/google/android/apps/location/gps/gnsslogger/pseudorange/ExampleUnitTest.java`:

```java
package com.google.android.apps.location.gps.gnsslogger.pseudorange;

import static org.junit.Assert.*;

import org.junit.Test;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
  @Test
  public void addition_isCorrect() {
    assertEquals(4, 2 + 2);
  }
}

```

`settings.gradle`:

```gradle
pluginManagement {
    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "GNSS Logger"
include ':app'
include ':pseudorange'

```