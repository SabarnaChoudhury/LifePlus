import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PatientService {
  // Use your JSON Blob URL here
  private baseUrl = 'http://jsonblob.com/api/jsonBlob/1289310206734229504';

  constructor(private http: HttpClient) {}

  // Fetch patient data from JSON Blob
  getPatients(): Observable<any> {
    return this.http.get<any>(this.baseUrl);
  }
}
