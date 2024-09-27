import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PatientListComponent } from './patient/patient-list/patient-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, PatientListComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']  // Corrected `styleUrls` instead of `styleUrl`
})
export class AppComponent {
  title = 'life-plus';
}
