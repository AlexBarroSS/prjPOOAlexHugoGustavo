/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fatec.poo.view;

import fatec.poo.control.Conexao;
import fatec.poo.control.DaoAluno;
import fatec.poo.control.DaoPessoa;
import fatec.poo.model.Aluno;
import fatec.poo.model.Pessoa;

import javax.swing.JOptionPane;
/**
 *
 * @author Gustavo
 */
public class GUIAluno extends javax.swing.JFrame {

    /**
     * Creates new form GUIAluno
     */
    public GUIAluno() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        btnConsultar = new javax.swing.JButton();
        btnInserir = new javax.swing.JButton();
        btnAlterar = new javax.swing.JButton();
        btnExcluir = new javax.swing.JButton();
        btnSair = new javax.swing.JButton();
        txtfEmail = new javax.swing.JTextField();
        txtfCidade = new javax.swing.JTextField();
        txtfBairro = new javax.swing.JTextField();
        txtfEndereço = new javax.swing.JTextField();
        txtfNome = new javax.swing.JTextField();
        ftfCPF = new javax.swing.JFormattedTextField();
        ftfRG = new javax.swing.JFormattedTextField();
        jLabel9 = new javax.swing.JLabel();
        cboxEstado = new javax.swing.JComboBox<>();
        cboxSexo = new javax.swing.JComboBox<>();
        jLabel10 = new javax.swing.JLabel();
        cboxEstCiv = new javax.swing.JComboBox<>();
        jLabel11 = new javax.swing.JLabel();
        txtfN = new javax.swing.JTextField();
        ftfCEP = new javax.swing.JFormattedTextField();
        ftfTelRes = new javax.swing.JFormattedTextField();
        ftfDtNasc = new javax.swing.JFormattedTextField();
        cboxEscol = new javax.swing.JComboBox<>();
        ftfCel = new javax.swing.JFormattedTextField();
        jLabel12 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        jLabel14 = new javax.swing.JLabel();
        jLabel15 = new javax.swing.JLabel();
        jLabel16 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Cadastrar Aluno");
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosed(java.awt.event.WindowEvent evt) {
                formWindowClosed(evt);
            }
            public void windowOpened(java.awt.event.WindowEvent evt) {
                formWindowOpened(evt);
            }
        });

        jLabel1.setText("CPF");

        jLabel2.setText("Nome");

        jLabel3.setText("Sexo");

        jLabel4.setText("Endereço");

        jLabel5.setText("Bairro");

        jLabel6.setText("Cidade");

        jLabel7.setText("RG");

        jLabel8.setText("Email");

        btnConsultar.setIcon(new javax.swing.ImageIcon(getClass().getResource("/fatec/poo/view/icon/pesq.png"))); // NOI18N
        btnConsultar.setText("Consultar");
        btnConsultar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnConsultarActionPerformed(evt);
            }
        });

        btnInserir.setIcon(new javax.swing.ImageIcon(getClass().getResource("/fatec/poo/view/icon/add.png"))); // NOI18N
        btnInserir.setText("Inserir");
        btnInserir.setEnabled(false);
        btnInserir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnInserirActionPerformed(evt);
            }
        });

        btnAlterar.setIcon(new javax.swing.ImageIcon(getClass().getResource("/fatec/poo/view/icon/Alterar.png"))); // NOI18N
        btnAlterar.setText("Alterar");
        btnAlterar.setEnabled(false);

        btnExcluir.setIcon(new javax.swing.ImageIcon(getClass().getResource("/fatec/poo/view/icon/Eraser.png"))); // NOI18N
        btnExcluir.setText("Excluir");
        btnExcluir.setEnabled(false);
        btnExcluir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnExcluirActionPerformed(evt);
            }
        });

        btnSair.setIcon(new javax.swing.ImageIcon(getClass().getResource("/fatec/poo/view/icon/exit.png"))); // NOI18N

        btnSair.setText("Sair");

        btnSair.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnSairActionPerformed(evt);
            }
        });

        txtfEmail.setEnabled(false);

        txtfCidade.setEnabled(false);

        txtfBairro.setEnabled(false);

        txtfEndereço.setEnabled(false);

        txtfNome.setEnabled(false);
        txtfNome.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtfNomeActionPerformed(evt);
            }
        });

        try {
            ftfCPF.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("###.###.###-##")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }

        try {
            ftfRG.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("##.###.###-#")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }
        ftfRG.setEnabled(false);

        jLabel9.setText("Estado");

        cboxEstado.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "SP", "RJ", "RR", "MG", "RS", "SC" }));
        cboxEstado.setEnabled(false);

        cboxSexo.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Masculino", "Feminino", " " }));
        cboxSexo.setEnabled(false);

        jLabel10.setText("Estado Civil");

        cboxEstCiv.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Solteiro(a)", "Casado(a)", "Divorciado(a)" }));
        cboxEstCiv.setEnabled(false);

        jLabel11.setText("Data Nascimento");

        txtfN.setEnabled(false);

        try {
            ftfCEP.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("#####-###")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }
        ftfCEP.setEnabled(false);

        try {
            ftfTelRes.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("(##)####- ####")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }
        ftfTelRes.setEnabled(false);

        try {
            ftfDtNasc.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("##/##/##")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }
        ftfDtNasc.setEnabled(false);
        ftfDtNasc.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ftfDtNascActionPerformed(evt);
            }
        });

        cboxEscol.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Ensino Fundamental", "Ensino Médio", "Ensino Superior" }));
        cboxEscol.setEnabled(false);

        try {
            ftfCel.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("(##)#####- ####")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }
        ftfCel.setEnabled(false);

        jLabel12.setText("Escolaridade");

        jLabel13.setText("N°");

        jLabel14.setText("CEP");

        jLabel15.setText("Tel. Res");

        jLabel16.setText("Celular");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(btnConsultar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(btnInserir)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(btnAlterar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(btnExcluir)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(btnSair))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabel4)
                            .addComponent(jLabel3)
                            .addComponent(jLabel2)
                            .addComponent(jLabel1)
                            .addComponent(jLabel5)
                            .addComponent(jLabel6)
                            .addComponent(jLabel7)
                            .addComponent(jLabel8))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                        .addComponent(txtfCidade, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGap(18, 18, 18)
                                        .addComponent(jLabel9)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(cboxEstado, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                                    .addComponent(txtfBairro, javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(txtfEndereço))
                                .addGap(42, 42, 42)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jLabel14)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(ftfCEP, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                                .addComponent(jLabel13)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                                .addComponent(txtfN, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))))
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jLabel15)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(ftfTelRes, javax.swing.GroupLayout.PREFERRED_SIZE, 102, javax.swing.GroupLayout.PREFERRED_SIZE))))
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(txtfEmail, javax.swing.GroupLayout.PREFERRED_SIZE, 230, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(ftfCPF, javax.swing.GroupLayout.PREFERRED_SIZE, 77, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(ftfRG, javax.swing.GroupLayout.PREFERRED_SIZE, 62, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(cboxSexo, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGap(18, 18, 18)
                                        .addComponent(jLabel10)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(cboxEstCiv, 0, 1, Short.MAX_VALUE))
                                    .addComponent(txtfNome, javax.swing.GroupLayout.PREFERRED_SIZE, 230, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jLabel16)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(ftfCel, javax.swing.GroupLayout.PREFERRED_SIZE, 102, javax.swing.GroupLayout.PREFERRED_SIZE))
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jLabel11)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(ftfDtNasc, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jLabel12)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(cboxEscol, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))))
                        .addGap(9, 9, 9)))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        layout.linkSize(javax.swing.SwingConstants.HORIZONTAL, new java.awt.Component[] {btnAlterar, btnConsultar, btnExcluir, btnInserir, btnSair});

        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(ftfCPF, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(txtfNome, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ftfDtNasc, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel11))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel3)
                    .addComponent(cboxSexo, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel10)
                    .addComponent(cboxEstCiv, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(cboxEscol, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel12))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(txtfEndereço, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtfN, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel13))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(txtfBairro, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ftfCEP, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel14))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(txtfCidade, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel9)
                    .addComponent(cboxEstado, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ftfTelRes, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel15))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel7)
                    .addComponent(ftfRG, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ftfCel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel16))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel8)
                    .addComponent(txtfEmail, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnConsultar)
                    .addComponent(btnInserir)
                    .addComponent(btnAlterar)
                    .addComponent(btnExcluir)
                    .addComponent(btnSair))
                .addGap(22, 22, 22))
        );

        layout.linkSize(javax.swing.SwingConstants.VERTICAL, new java.awt.Component[] {btnAlterar, btnConsultar, btnExcluir, btnInserir, btnSair});

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void txtfNomeActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtfNomeActionPerformed

    }//GEN-LAST:event_txtfNomeActionPerformed

    private void btnSairActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnSairActionPerformed

    }//GEN-LAST:event_btnSairActionPerformed

    private void formWindowOpened(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowOpened
        conexao = new Conexao("alex","alex1234");
        conexao.setDriver("oracle.jdbc.driver.OracleDriver");
        conexao.setConnectionString("jdbc:oracle:thin:@localhost:1521:xe"); 
        daoAluno = new DaoAluno(conexao.conectar());
        daoPessoa = new DaoPessoa(conexao.conectar());
    }//GEN-LAST:event_formWindowOpened

    private void formWindowClosed(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowClosed
        conexao.fecharConexao();
        dispose();
    }//GEN-LAST:event_formWindowClosed

    private void btnConsultarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnConsultarActionPerformed
        cpf = ftfCPF.getText().replaceAll("[.,-]", "");

        
        if(Pessoa.validarCPF(cpf) == true){
            pessoa = null;
            aluno = null;
            pessoa = daoPessoa.consultar(cpf);
            aluno = daoAluno.Consultar(cpf);
            
            if (aluno == null){
                ftfCPF.setEnabled(false);
                txtfNome.setEnabled(true);
                cboxEstCiv.setEnabled(true);
                txtfEndereço.setEnabled(true);
                ftfDtNasc.setEnabled(true);
                cboxSexo.setEnabled(true);
                txtfN.setEnabled(true);
                txtfBairro.setEnabled(true);
                ftfCEP.setEnabled(true);
                txtfCidade.setEnabled(true);
                cboxEstado.setEnabled(true);
                ftfRG.setEnabled(true);
                cboxEscol.setEnabled(true);
                txtfEmail.setEnabled(true);
                ftfTelRes.setEnabled(true);
                ftfCel.setEnabled(true);
                txtfNome.requestFocus();
            
                btnConsultar.setEnabled(false);
                btnAlterar.setEnabled(false);
                btnExcluir.setEnabled(false);
                btnInserir.setEnabled(true);
        }
        else {
            txtfNome.setText(pessoa.getNome());
            cboxEstCiv.setSelectedItem(pessoa.getEstadoCivil());
            txtfEndereço.setText(pessoa.getEndereco());
            ftfDtNasc.setText(pessoa.getDataNasc());
            cboxSexo.setSelectedItem(pessoa.getSexo());
            txtfN.setText(Integer.toString(pessoa.getNumero()));
            txtfBairro.setText(pessoa.getBairro());
            ftfCEP.setText(pessoa.getCEP());
            txtfCidade.setText(pessoa.getCidade());
            cboxEstado.setSelectedItem(pessoa.getEstado());
            ftfRG.setText(pessoa.getRG());
            cboxEscol.setSelectedItem(pessoa.getRG());
            txtfEmail.setText(pessoa.getEmail());
            ftfTelRes.setText(pessoa.getTelefone());
            ftfCel.setText(pessoa.getCelular());
            
            btnConsultar.setEnabled(false);
            btnInserir.setEnabled(false);
            btnAlterar.setEnabled(true);
            btnExcluir.setEnabled(true);
            }
        } else{
            JOptionPane.showMessageDialog(null, "CPF inserido não é válido.");
        }

    }//GEN-LAST:event_btnConsultarActionPerformed

    private void ftfDtNascActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ftfDtNascActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ftfDtNascActionPerformed

    private void btnInserirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnInserirActionPerformed
        pessoa = new Pessoa(cpf, txtfNome.getText());
        aluno = new Aluno(cpf, txtfNome.getText());
        
        pessoa.setCPF(cpf);
        pessoa.setNome(txtfNome.getText());
        pessoa.setDataNasc(ftfDtNasc.getText());
        pessoa.setEndereco(txtfEndereço.getText());
        pessoa.setNumero(Integer.parseInt(txtfN.getText()));
        pessoa.setBairro(txtfBairro.getText());
        pessoa.setCidade(txtfCidade.getText());
        pessoa.setEstado(cboxEstado.getSelectedItem().toString());
        pessoa.setCEP(ftfCEP.getText().replaceAll("[-]", ""));
        pessoa.setTelefone(ftfTelRes.getText().replaceAll("[(,),-]", ""));
        pessoa.setCelular(ftfCel.getText().replaceAll("[(,),-]", ""));
        pessoa.setSexo(cboxSexo.getSelectedItem().toString());
        pessoa.setEstadoCivil(cboxEstCiv.getSelectedItem().toString());
        pessoa.setRG(ftfRG.getText().replaceAll("[.,-]", ""));
        pessoa.setEmail(txtfEmail.getText());
           
        aluno.setCPF(cpf);
        aluno.setEscolaridade((String) cboxEscol.getSelectedItem());
           
        
        daoPessoa.inserir(pessoa);
        daoAluno.Inserir(aluno);
        
        ftfCPF.setText("");
        txtfNome.setText("");
        cboxEstCiv.setSelectedIndex(0x0);
        txtfEndereço.setText("");
        ftfDtNasc.setText("");
        cboxSexo.setSelectedIndex(0x0);
        txtfN.setText("");
        txtfBairro.setText("");
        ftfCEP.setText("");
        txtfCidade.setText("");
        cboxEstado.setSelectedIndex(0x0);
        ftfRG.setText("");
        cboxEscol.setSelectedItem("");
        txtfEmail.setText("");
        ftfTelRes.setText("");
        ftfCel.setText("");
        
        btnConsultar.setEnabled(true);
        btnInserir.setEnabled(false);

    }//GEN-LAST:event_btnInserirActionPerformed

    private void btnExcluirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnExcluirActionPerformed
        if (JOptionPane.showConfirmDialog(null, "Confirma Alteração?") == 0){
            daoAluno.Excluir(aluno.getCPF());
        }
        
        ftfCPF.setText("");
        txtfNome.setText("");
        cboxEstCiv.setSelectedIndex(0x0);
        txtfEndereço.setText("");
        ftfDtNasc.setText("");
        cboxSexo.setSelectedIndex(0x0);
        txtfN.setText("");
        txtfBairro.setText("");
        ftfCEP.setText("");
        txtfCidade.setText("");
        cboxEstado.setSelectedIndex(0x0);
        ftfRG.setText("");
        cboxEscol.setSelectedItem("");
        txtfEmail.setText("");
        ftfTelRes.setText("");
        ftfCel.setText("");
             
        ftfCPF.setEnabled(true);
        txtfNome.setEnabled(false);
        cboxEstCiv.setEnabled(false);
        txtfEndereço.setEnabled(false);
        ftfDtNasc.setEnabled(false);
        cboxSexo.setEnabled(false);
        txtfN.setEnabled(false);
        txtfBairro.setEnabled(false);
        ftfCEP.setEnabled(false);
        txtfCidade.setEnabled(false);
        cboxEstado.setEnabled(false);
        ftfRG.setEnabled(false);
        cboxEscol.setEnabled(false);
        txtfEmail.setEnabled(false);
        ftfTelRes.setEnabled(false);
        ftfCel.setEnabled(false);
        ftfCPF.requestFocus();
        
        btnConsultar.setEnabled(true);
        btnInserir.setEnabled(false);
        btnAlterar.setEnabled(false);
        btnExcluir.setEnabled(false);

    }//GEN-LAST:event_btnExcluirActionPerformed

    public static void main(String args[]) {
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(GUIAluno.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(GUIAluno.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(GUIAluno.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(GUIAluno.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new GUIAluno().setVisible(true);
            }
        });
    }
    

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAlterar;
    private javax.swing.JButton btnConsultar;
    private javax.swing.JButton btnExcluir;
    private javax.swing.JButton btnInserir;
    private javax.swing.JButton btnSair;
    private javax.swing.JComboBox<String> cboxEscol;
    private javax.swing.JComboBox<String> cboxEstCiv;
    private javax.swing.JComboBox<String> cboxEstado;
    private javax.swing.JComboBox<String> cboxSexo;
    private javax.swing.JFormattedTextField ftfCEP;
    private javax.swing.JFormattedTextField ftfCPF;
    private javax.swing.JFormattedTextField ftfCel;
    private javax.swing.JFormattedTextField ftfDtNasc;
    private javax.swing.JFormattedTextField ftfRG;
    private javax.swing.JFormattedTextField ftfTelRes;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel14;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel16;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JTextField txtfBairro;
    private javax.swing.JTextField txtfCidade;
    private javax.swing.JTextField txtfEmail;
    private javax.swing.JTextField txtfEndereço;
    private javax.swing.JTextField txtfN;
    private javax.swing.JTextField txtfNome;
    // End of variables declaration//GEN-END:variables
    private Conexao conexao;
    private DaoAluno daoAluno;
    private DaoPessoa daoPessoa;
    private Pessoa pessoa;
    private Aluno aluno;
    private String cpf;
}
