import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl = 'http://127.0.0.1:8000';
  token = 'Token ce0648b6a8e0e3fe603648c0f2c7969cdddbb756';
  httpHeaders = new HttpHeaders().set('Content-Type', 'application/json').set('Authorization', this.token);

  constructor(private requests: HttpClient) { }

  newRestaurant(restaurant): Observable<any>{
    return this.requests.post(this.baseUrl + '/restaurant/', restaurant,{headers: this.httpHeaders});
  };

  newContact(contact): Observable<any>{
    return this.requests.post(this.baseUrl + '/contact/', contact, {headers: this.httpHeaders});
  };
}
