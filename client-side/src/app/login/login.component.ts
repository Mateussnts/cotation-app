import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor( private http: HttpClient) { }

  
  //this.http.post('http://127.0.0.1:8000/api/login')

  ngOnInit(): void {
  }

}
