import { Component, OnInit } from '@angular/core';
import { PatientService } from '../patient.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-patient-list',
  templateUrl: './patient-list.component.html',
  styleUrls: ['./patient-list.component.scss'],
  standalone: true,  // Mark the component as standalone
  imports: [CommonModule],  // Add required imports like CommonModule
})
export class PatientListComponent implements OnInit {
  patients: any[] = [];  // Define an empty array to hold patient data

  constructor(private patientService: PatientService) {}

  ngOnInit(): void {
    // Fetch patients from JSON Blob
    this.patientService.getPatients().subscribe((data) => {
      this.patients = data.patients;  // Use 'data.patients' since our JSON is nested
    });
  }
}
