import {Injectable} from '@angular/core';
import { HttpClient, HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { CanActivate, Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { tap, shareReplay } from 'rxjs/operators';
import * as jwtDecode from 'jwt-decode';
import * as moment from 'moment';
import { environment } from './environments/environment'

@Injectable({providedIn: 'root'})

export class AuthService {
    private apiURL = 'http://127.0.0.1:8000/api/'

    constructor(private httpClient: HttpClient){}

    login(email: string, password: string){
        return this.httpClient.post(this.apiURL.concat('/login'), {email, password});
    }

    signup(nome: string, email: string, password: string){
        return this.httpClient.post(this.apiURL.concat('/register'),{});
    }

}