import { Component, OnInit } from '@angular/core';
import  { Router } from '@angular/router';
import { AuthService } from 'src/authService';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.scss']
})
export class CadastroComponent implements OnInit {

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
  }

  signup(nome: string, email: string, password: string){
    this.authService.signup(nome, email, password).subscribe(
      success => this.router.navigate(['login']));
  }
}

